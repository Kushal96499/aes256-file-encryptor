# 🔐 AES-256 File Encryptor & Decryptor

A secure and beginner-friendly **Python** tool to **Encrypt** and **Decrypt** your files using the **AES-256 encryption standard**.  
Comes with a **simple GUI** built using **Tkinter**!

---

## ✨ Features

- 🔒 AES-256 Secure Encryption
- 🖥️ Simple Graphical User Interface (GUI)
- 📂 File Selection through Dialog Box
- 🔑 Authentication via Nonce and Tag
- ⚙️ Full Error Handling and User Feedback
- 📦 Lightweight and Fast

---

## 📋 Requirements

- Python 3.x
- Required Libraries:
  - `pycryptodome`
  - `tkinter` (comes pre-installed with Python)

To install `pycryptodome`, run:
```bash
pip install pycryptodome
```
---

## 🚀 How to Run
Clone this repository or download the files.

Open your terminal and navigate to the project directory.

Run the application:
```bash
python gui_file_encryptor.py
```
Select your file.

Enter a 32-character secret key.

Choose whether you want to Encrypt or Decrypt.

Done!

---
## ⚠️ Important Notes
Your secret key must be exactly 32 characters long for AES-256.

Encrypted files will have a .enc extension.

Decrypted files will have a .dec extension.

Always remember your key. Lost keys = lost data!

---

## 📂 Project Structure

File Name	             Description
gui_file_encryptor.py	 Main Python script for the tool
README.md	             Project description and usage guide

---

## 🛡️ Disclaimer
This tool is designed for educational purposes and basic file security.
Do not use for critical or government-level encryption without proper security audits.

---

## 🤝 Credits
Developed during CODTECH Cyber Security Internship.
Crafted with ❤️ to empower beginners in cybersecurity.
