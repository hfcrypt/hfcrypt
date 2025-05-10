import os
import sys
import zipfile
from pathlib import Path
import click
from cryptography.fernet import Fernet
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from io import BytesIO
import shutil
import yaml
import huggingface_hub as hub

def generate_key(password: str) -> bytes:
    """Generate encryption key from password"""
    salt = b'hfcrypt_salt'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def process_readme(readme_path: str) -> str:
    """Process README.md to replace sdk with docker if YAML frontmatter exists"""
    try:
        with open(readme_path, 'r') as f:
            content = f.read()
            
        if not content.startswith('---'):
            return content
            
        # Split frontmatter and content
        parts = content.split('---', 2)
        if len(parts) < 3:
            return content
            
        frontmatter = parts[1]
        rest = parts[2]
        
        try:
            # Parse YAML frontmatter
            yaml_data = yaml.safe_load(frontmatter)
            if yaml_data and 'sdk' in yaml_data:
                yaml_data['sdk'] = 'docker'
                # Reconstruct the file
                return f"---\n{yaml.dump(yaml_data)}---{rest}"
        except yaml.YAMLError:
            click.echo("Warning: Invalid YAML frontmatter in README.md")
            return content
            
    except Exception as e:
        click.echo(f"Warning: Error processing README.md: {str(e)}")
        return content

def encrypt_folder(input_folder: str, output_folder: str, password: str):
    """Zip and encrypt a folder"""
    # Create output directory if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Generate encryption key
    key = generate_key(password)
    f = Fernet(key)
    
    # Create zip file in memory
    zip_buffer = BytesIO()
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, _, files in os.walk(input_folder):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, input_folder)
                zip_file.write(file_path, arcname)
    
    # Encrypt the zip file
    encrypted_data = f.encrypt(zip_buffer.getvalue())
    
    # Save encrypted file
    output_path = os.path.join(output_folder, 'app.hfc')
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    # Copy individual files from templates directory to output folder
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    if os.path.exists(templates_dir):
        for item in os.listdir(templates_dir):
            src_path = os.path.join(templates_dir, item)
            dst_path = os.path.join(output_folder, item)
            if os.path.isfile(src_path):
                shutil.copy2(src_path, dst_path)
            elif os.path.isdir(src_path):
                shutil.copytree(src_path, dst_path, dirs_exist_ok=True)
    
    # Copy and process README.md from input folder if it exists
    readme_path = os.path.join(input_folder, 'README.md')
    if os.path.exists(readme_path):
        processed_content = process_readme(readme_path)
        with open(os.path.join(output_folder, 'README.md'), 'w') as f:
            f.write(processed_content)

@click.command()
@click.argument('input_folder')
@click.argument('output_folder')
def app(input_folder: str, output_folder: str):
    """Zip and encrypt a folder with password protection"""
    # Check if output folder exists and contains files
    if os.path.exists(output_folder) and os.listdir(output_folder):
        if not click.confirm(f'Output folder {output_folder} already exists and contains files. Continue?', default=False):
            click.echo('Operation cancelled.')
            return
    
    password = click.prompt('Enter encryption password', hide_input=True)
    encrypt_folder(input_folder, output_folder, password)
    click.echo(f'Successfully encrypted {input_folder} to {output_folder}')
    
    # Ask if user wants to push to HF space
    if click.confirm('Would you like to push this to a Hugging Face Space?', default=False):
        repo_id = click.prompt('Enter the repository ID (username/repo-name)')
        if not hub.repo_exists(repo_id, repo_type='space'):
            private = click.confirm('Make this space private?', default=False)
            hub.create_repo(repo_id, repo_type='space', space_sdk='docker', private=private)

        click.echo(f'Pushing to {repo_id}')
        hub.upload_folder(folder_path=output_folder, repo_id=repo_id, repo_type='space')
        hub.add_space_secret(repo_id, 'HFCRYPT_KEY', password)
        click.echo(f'Successfully pushed to {repo_id}')

if __name__ == '__main__':
    app()
