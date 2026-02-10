# 🔐 Simple Password Manager

## Introduction
This project is a minimal local password manager written in Python that demonstrates practical encryption using Fernet symmetric cryptography. It is intentionally simple, offline-only, and file-based, focusing on clarity and correctness rather than feature overload or production-grade complexity.

## Purpose
The goal of this project is to help learners understand how encryption keys, master passwords, and encrypted storage work together in a real program, avoiding fake security patterns such as plain-text storage or reversible encodings, while keeping the implementation readable and auditable.

## Technology Stack
The application is built using Python 3 and the `cryptography` library, specifically the Fernet module which provides authenticated symmetric encryption based on AES, with local file storage used to persist encrypted credentials and the generated encryption key.

## How It Works
A secret key is generated once and stored in a local file, the user provides a master password at runtime, and the program combines both to create an encryption context that is used to encrypt passwords before writing them to disk and decrypt them only when the correct master password is supplied.

## Features
The password manager allows users to add new credentials, encrypts passwords before storage, decrypts them on demand for viewing, operates entirely offline, and avoids external services, databases, or network communication.

## Usage
After installing the required dependency and generating the encryption key once, the user runs the program, enters a master password, and interacts with the application through a command-line interface to add or view stored passwords until choosing to exit.

## Security Notes
This project is designed for educational purposes and does not implement advanced security measures such as key derivation functions, hashing, salting, password masking, or recovery mechanisms, meaning that losing the key file or forgetting the master password will permanently lock all stored data.

## Limitations
The application lacks password strength validation, update or delete functionality, structured storage formats, robust error handling, and protections against file corruption, all of which are deliberately omitted to keep the core encryption logic exposed and understandable.

## License
This project is free to use, modify, and extend for learning and experimentation, with no warranty or guarantee of suitability for production environments.
