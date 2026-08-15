import os
from cryptography.fernet import Fernet

# Decryptor

files = []

for file in os.listdir():
    if file in {"main.py", "secret.key", "decrypt.py", "test.py"}:
         continue
    
    if os.path.isfile(file):
        files.append(file)

    
decryption_key = input("Key: ").encode()

for file in files:
    with open(file, "rb") as thefile:
        file_content = thefile.read()

    contents_decrypted = Fernet(decryption_key).decrypt(file_content)

    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

