# Cybersecurity Python Projects
This repository contains three beginner-friendly cybersecurity projects written in Python.

The purpose of this repo is to demonstrate hands-on experience with core security concepts such as network reconnaissance, log analysis, and password security.

## Projects Included

## 1. Network Port Scanner

A simple TCP port scanner that checks a target host for open ports from 1 to 1024.

### Concepts demonstrated

- Socket programming
- TCP connections
- Network service discovery
- Basic reconnaissance

## 2. Security Log Analyzer

A Python script that reads a sample log file and identifies failed login attempts.

### Concepts demonstrated

- Log analysis
- Authentication monitoring
- Suspicious activity detection
- Basic threat identification

## 3. Password Security Analyzer

A Python tool that evaluates password strength based on length and character diversity.

### Concepts Demonstrated

- Password security principles
- Input validation
- Regular expressions
- Credential security awareness
---

## Repository Structure

```
cybersecurity-python-projects/
│
├── README.md
│
├── port-scanner/
│   ├── port_scanner.py
│   └── README.md
│
├── log-analyzer/
│   ├── log_analyzer.py
│   ├── server_log.txt
│   └── README.md
│
└── password-analyzer/
    ├── password_analyzer.py
    └── README.md
```

---

## Requirements

- Python 3.x
- No external libraries required. All projects use Python standard library modules only.

How to Use
Clone the repository or download the ZIP file, then navigate into any project folder and run the script with Python 3.

Example:

python3 port_scanner.py
Why I Built This Repo
I created these projects to strengthen my understanding of cybersecurity and networking fundamentals through hands-on Python scripting.
These projects reflect my interest in areas such as:

Network security
Threat monitoring
Vulnerability awareness
Authentication and access control
Future Improvements
Possible enhancements for this repository include:

Adding a banner grabber or service detection tool to the port scanner
Detecting repeated failed attempts from the same IP in the log analyzer
Adding entropy scoring and password suggestions to the password analyzer
Creating a simple command-line menu to launch each project from one place
Disclaimer
These projects are for educational purposes only.
Do not scan, test, or analyze systems without authorization.
