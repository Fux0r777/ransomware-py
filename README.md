# EncryptorPy

PYTHON RANSOMWARE

---

## Overview

This repository contains a demonstration of ransomware concepts implemented in Python, along with a simple PHP endpoint for receiving a generated encryption key (C2)
This is made for Linux but i suppose it works with WSL too.
created by SQL

## Contents

- ransomware.py  main Python file for the encryption and key transmission to the C2
- php-endpoint/  PHP web endpoint.
- php-endpoint/upload/upload.php the PHP receiver script.
- php-endpoint/HOW-TO-START.md  quick instructions to start the local PHP server.


## How To

1. Create a disposable test directory and put whatever worthless files in it. Do NOT run this on any important files or systems.
2. Copy `ransomware.py` into that directory.
3. Start the PHP endpoint (if you want to capture the generated key) from the `php-endpoint` folder:

   ```bash
   cd php-endpoint
   php -S 127.0.0.1:8000
   ```

4. In your test folder, run the Python script:

   ```bash
   python3 ransomware.py
   ```

5. The script encrypts files in the current directory (excluding a few filenames) and will POST the generated key to `http://127.0.0.1:8000/upload/upload.php` when the local endpoint is running.

## License

MIT :)

---


## Security & Safety (Important)

This repository contains code that implements destructive behavior (ransomware). The code is provided strictly for research, education, and defensive testing purposes only.

- Intended use
  - This project is intended only for academic study, analysis, and the development of defensive measures (for example, malware analysis, detection testing, or incident response practice).
  - Do NOT use this code to attack, extort, damage, or otherwise interfere with computers, networks, or data that you do not own or do not have explicit, written permission to test.

- Legal & ethical restrictions
  - Running or deploying this code without explicit authorization may be illegal and unethical. You are responsible for understanding and complying with all applicable laws and policies in your jurisdiction.
  - The author does not endorse or support malicious use of this code.

- Recommended safe testing practices
  - Only run this code in isolated, controlled environments such as disposable virtual machines or sandboxed lab networks that are physically or logically separated from production systems and sensitive data.
  - Use snapshots, clean restores, and air-gapped networks whenever possible so you can fully recover your test environment.
  - Do not connect test environments to corporate networks, cloud storage, or any systems containing real personal, corporate, or sensitive data.

- Disclaimer & liability
  - Use this repository at your own risk. The author and repository maintainers are not responsible or liable for any damage, data loss, legal consequences, or other harm resulting from use, misuse, or unintended consequences.

- Responsible disclosure & contact
  - If you discover vulnerabilities, unintended destructive behavior, or accidental data exposure related to this project, please report them responsibly by opening a GitHub issue or contacting the repository owner.


(im gonna be honest i did not write all dis shi)
