# 🔐 Simple Password Manager (Python + Fernet Encryption)

A minimal, local password manager built with Python.  
No cloud. No tracking. No drama.  
Just encryption, files, and your discipline.

This project uses **Fernet symmetric encryption** from the `cryptography` library to securely store and retrieve passwords using a **master password + key file**.

---

## 📌 Why This Exists

Most beginners learn encryption in theory and never touch it in practice.  
This project fixes that.

It teaches:
- How **real encryption** works (not fake Base64 nonsense)
- How **keys** and **passwords** interact
- Why security is more than just “hiding text”

Simple enough to understand.  
Serious enough to respect.

---

## ⚙️ Features

- 🔑 Generates and stores an encryption key (once)
- 🔒 Encrypts passwords using **Fernet**
- 📁 Stores encrypted data locally in a text file
- 👀 View and decrypt stored passwords
- ❌ No internet, no servers, no dependencies beyond crypto

---

## 🧠 How It Works (High-Level)

1. A **key** is generated once and saved in `key.key`
2. User enters a **master password**
3. The key + master password form the encryption secret
4. Passwords are:
   - Encrypted before saving
   - Decrypted only with the correct master password

Wrong password?  
You get garbage. As it should be.

---

## 🧰 Tech Stack

- **Language:** Python 3
- **Library:** `cryptography`
- **Encryption:** Fernet (AES under the hood)
- **Storage:** Local text file

No frameworks. No fluff.

---

## 📦 Requirements

Install the required library:

```bash
pip install cryptography
write_key()
key.key
python password_manager.py


