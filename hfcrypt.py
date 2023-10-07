print("""
  _    _ ______ _____                  _   
 | |  | |  ____/ ____|                | |  
 | |__| | |__ | |     _ __ _   _ _ __ | |_ 
 |  __  |  __|| |    | '__| | | | '_ \| __|
 | |  | | |   | |____| |  | |_| | |_) | |_ 
 |_|  |_|_|    \_____|_|   \__, | .__/ \__|
                            __/ | |        
                           |___/|_|        
HFCrypt: host closed-source apps on Hugging Face Spaces!

IMPORTANT! Make sure you're app's external port is set to "7860"!""")
import os
import sys
import zipfile
import shutil
from cryptography.fernet import Fernet
if not os.path.exists('app'):
    print('Unable to locate your app in the "app" directory.')
    sys.exit(0)
if not os.path.exists('app/app.py'):
    print('Unable to locate your app file in the "app/app.py" file.')
    sys.exit(0)
key = Fernet.generate_key()
folder_to_zip = 'app'
zip_filename = 'app.hfc'
print('What is the title of your app?')
title = input('Title > ')
print('Compressing app...')
with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(folder_to_zip):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, folder_to_zip)
            zipf.write(file_path, arcname)
print('Opening encrypted file...')
with open(zip_filename, 'rb') as file:
    data = file.read()
cipher_suite = Fernet(key)
print('Encrypting file...')
encrypted_data = cipher_suite.encrypt(data)
with open(zip_filename, 'wb') as file:
    file.write(encrypted_data)
print(f'Copying template...')
shutil.copytree('template', 'out')
with open('out/README.md', 'r+') as f:
    f.write(f.read().replace('__TITLE__', title))
shutil.copy('app.hfc', 'out')
print(f'Your key is:')
print(key.decode())
print('HFCrypt is done!')