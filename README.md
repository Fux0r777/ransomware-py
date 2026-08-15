# python-ransomware

Python ransomware demonstration (educational purposes only).

---

## Overview

This repository contains a small, controlled demonstration of ransomware concepts implemented in Python, along with a simple PHP endpoint for receiving a generated encryption key.

This project is intended for research, education, and defensive testing in isolated environments only. Do not run this code on systems or files you do not own or have explicit permission to test.


## Contents

- ransomware.py — main Python script demonstrating file encryption and key transmission.
- php-endpoint/ — simple PHP web endpoint to receive the encryption key (for local testing).
- php-endpoint/upload/upload.php — the PHP receiver script.
- php-endpoint/HOW-TO-START.md — quick instructions to start the local PHP server.


## Quick start (local, safe testing only)

1. Create a disposable test directory and put some dummy files in it. Do NOT run this on any important files or systems.
2. Copy `ransomware.py` into that directory.
3. Start the PHP endpoint (if you want to capture the generated key) from the `php-endpoint` folder:

   ```bash
   cd php-endpoint
   php -S 127.0.0.1:8000
   ```

4. In your test folder, run the Python script (inside an isolated VM or disposable environment):

   ```bash
   python3 ransomware.py
   ```

5. The script encrypts files in the current directory (excluding a few safe filenames) and will POST the generated key to `http://127.0.0.1:8000/upload/upload.php` when the local endpoint is running.


## Notes

- The script is intentionally simple and is provided to demonstrate concepts such as symmetric key generation and basic file encryption with the `cryptography` library.
- This is NOT production or real ransomware code. It lacks many safety checks and protections — it is destructive by design for demonstration purposes.


## License

(Include license or leave as desired.)


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
