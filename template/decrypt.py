from cryptography.fernet import Fernet
import zipfile
import os
key = os.environ["HFCRYPT_KEY"]
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
