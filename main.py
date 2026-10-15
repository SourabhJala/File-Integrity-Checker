#!/usr/bin/env python3
"""
Sourang File Integrity Checker
================================
Main Application Entry Point.
Supports:
- 3D Interactive Cyber-Vault Web GUI (`python main.py gui`)
- Native Desktop Tkinter GUI (`python main.py desktop`)
- Terminal CLI Verification Engine (`python main.py baseline`, `python main.py verify`)
- Tamper Simulation Demonstrator (`python main.py simulate`)
- Interactive Menu (simply run `python main.py`)
"""

import sys
from sourang_integrity.cli import main

if __name__ == "__main__":
    main()
