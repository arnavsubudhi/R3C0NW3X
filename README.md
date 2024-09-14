# R3C0NW3X

## Overview
R3C0NW3X is a fully automated pentesting tool designed to streamline the process of identifying, weaponizing, and exploiting vulnerabilities. The tool presents three main functionalities:
1. **Recon**: Information gathering from a person's name, IP address, and detection of open ports and services.
2. **Weaponization**: Searching for relevant exploits and downloading them.
3. **Exploitation**: Performing various brute-force attacks to gain access or control.

## Features
- **Automated Recon**: Gather target information based on a person's name, IP address, and identify open ports and services.
- **Weaponization**: Automatically search for known exploits based on gathered information and download them for use.
- **Exploitation**: Execute exploits and perform SSH brute-force, subdomain brute-force, and directory brute-force attacks.
- **User-friendly CLI**: Easy to navigate with a clear set of options for each phase of the pentesting process.

## Installation and Usage

### Prerequisites
Before using **R3C0NW3X**, ensure you have the following:
- **Python 3**
- **Any additional dependencies listed in the `requirements.txt` file**

### Usage

```bash
git clone https://github.com/yourusername/R3C0NW3X.git
cd R3C0NW3X
pip install -r requirements.txt or pip3 install -r requirements.txt
python3 r3c0nw3x.py

