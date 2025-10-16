# Py to Exe - Quick Converter [GUI]

GUI tool to convert Python `.py` files to Windows `.exe` using PyInstaller.

## Features
- Simple GUI for PyInstaller
- One-file `.exe` or folder
- Clear cache & remove spec file options
- Supports custom icon
- Shows real-time log
- Handles multiple conversions safely (prevents conflicts if PyInstaller is still running from a previous conversion)

## Requirements
- Python 3.10+
- PyQt6 (6.9.1)
- psutil (7.1.0)
- PyInstaller (6.16.0)

Install dependencies:
```bash
pip install -r requirements.txt
