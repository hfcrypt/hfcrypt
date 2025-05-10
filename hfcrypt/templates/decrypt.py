from cryptography.fernet import Fernet
import zipfile
import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

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

password = os.environ["HFCRYPT_KEY"]
key = generate_key(password)
encrypted_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app.hfc'))

with open(encrypted_filename, 'rb') as file:
    encrypted_data = file.read()

cipher_suite = Fernet(key)
decrypted_data = cipher_suite.decrypt(encrypted_data)

decrypted_output_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'out.zip'))

with open(decrypted_output_filename, 'wb') as file:
    file.write(decrypted_data)

with zipfile.ZipFile(decrypted_output_filename, 'r') as zip_ref:
    zip_ref.extractall(os.path.abspath(os.path.join(os.path.dirname(__file__), 'hfapp')))