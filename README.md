📘 Password Strength Manager — README.md
🔐 Overview
The Password Strength Manager is a security‑focused Flask application designed to evaluate password strength, generate secure passwords, and check for known breaches using the HaveIBeenPwned API.
This project was built as part of an academic cybersecurity unit, following secure coding practices and DevSecOps principles.

The system includes:

User authentication with bcrypt hashing

Password strength analysis (entropy, patterns, dictionary checks)

Secure password generator

Breach detection using k‑Anonymity (HIBP)

CI/CD pipeline with Bandit, pip‑audit, pytest, and OWASP ZAP

📁 Project Structure
Code
src/
│── app.py
│
├── auth/
│   ├── routes.py
│   ├── models.py
│   └── __init__.py
│
├── strength/
│   ├── entropy.py
│   ├── scoring.py
│   ├── patterns.py
│   ├── dictionary_check.py
│   └── routes.py
│
├── generator/
│   ├── generator.py
│   └── routes.py
│
└── breach_check/
    ├── breach.py
    └── routes.py
🚀 Features
🔑 Authentication Module
Secure login

bcrypt password hashing

Role‑based access control (RBAC)

Optional 2FA support

🧠 Password Strength Module
Entropy calculation

Complexity scoring

Pattern detection (repeated chars, sequences, weak words)

Dictionary attack simulation

🔒 Password Generator
Cryptographically secure (using secrets)

Customizable length and character sets

API endpoint: /generator/create

🛡 Breach Check (HaveIBeenPwned)
SHA‑1 hashing

k‑Anonymity lookup

No password ever leaves the server

API endpoint: /breach/check

🔧 CI/CD Pipeline
Runs automatically on every push:

Bandit — static code analysis

pip‑audit — dependency vulnerability scan

pytest — automated tests

OWASP ZAP — baseline DAST scan

GitHub Actions workflow

📡 API Endpoints
Authentication
Method	Endpoint	Description
POST	/auth/login	User login
POST	/auth/register	Register new user


Password Strength
Method	Endpoint	Description
POST	/strength/check	Analyze password strength


Password Generator
Method	Endpoint	Description
POST	/generator/create	Generate secure password


Breach Check
Method	Endpoint	Description
POST	/breach/check	Check if password is leaked


🧪 Testing the API
Example PowerShell request:

powershell
Invoke-WebRequest -Uri "http://127.0.0.1:5000/strength/check" `
  -Method POST `
  -Headers @{ "Content-Type" = "application/json" } `
  -Body '{"password":"Admin@123"}' `
  -UseBasicParsing
⚙️ Running the Application
Install dependencies:
cmd
pip install -r requirements.txt
Start the server:
cmd
py src/app.py
🔄 CI/CD Pipeline
Located at:

Code
.github/workflows/ci.yml
Includes:

Bandit security scan

pip‑audit dependency scan

pytest unit tests

OWASP ZAP baseline scan

This ensures continuous security and code quality.

📚 Technologies Used
Python 3.12

Flask

bcrypt

secrets

requests

GitHub Actions

Bandit

pip‑audit

pytest

OWASP ZAP

👨‍🎓 Author
Sunil Dahal  
Master of Information Technology
Crown Institute of Higher Education