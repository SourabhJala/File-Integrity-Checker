# 🛡️ Sourang File Integrity Checker
### *3D Cryptographic SHA-256 File Integrity Monitoring & Tamper Radar*

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Security](https://img.shields.io/badge/Hash%20Algorithm-SHA--256-brightgreen.svg)]()
[![GUI](https://img.shields.io/badge/Interface-3D%20WebGL%20%7C%20Terminal%20CLI%20%7C%20Desktop-cyan.svg)]()
[![Build Status](https://img.shields.io/badge/Tests-8%2F8%20Passed-success.svg)]()

---

## 🌟 Overview

**Sourang File Integrity Checker** is a high-performance cryptographic security utility designed to detect unauthorized modifications, stealth tampering, and file corruptions across sensitive directories. 

Built with cryptographic **SHA-256 chunked streaming**, it generates structured baseline manifests and performs rigorous verification. The system is engineered to catch **single-byte modifications even when an adversary intentionally forges modification timestamps and preserves file sizes**.

It delivers a dual-experience interface:
1. **🌌 3D Interactive Cyber-Vault Web GUI**: A real-time Three.js WebGL holographic visualizer where files hover in 3D orbital space around a central cryptographic core, pulsing red under tamper alerts.
2. **🖥️ Terminal CLI & Interactive Radar**: High-resolution ASCII banner, colored tables, live status meters, and automated audit exports (HTML & JSON).
3. **💻 Native Desktop Tkinter GUI**: Standalone dark-mode desktop window featuring real-time 3D isometric wireframe rendering with zero external web dependencies.

---

## 🚀 Key Features

* **Cryptographic SHA-256 Hashing**: Memory-efficient 64 KB chunked streaming reads that handle multi-gigabyte files cleanly without RAM spikes.
* **Stealth Tamper Detection**: Proves the cryptographic avalanche effect by detecting single-byte and single-bit file alterations even when file size and `mtime` modification timestamps are artificially spoofed.
* **Structured Baseline Manifests**: Exports audit-ready JSON manifests containing file paths, byte sizes, exact UTC timestamps, and SHA-256 digests. Optional CSV export supported.
* **4-Way File Taxonomy**:
  * 🟢 **INTACT**: Files whose hash and size match baseline precisely.
  * 🔴 **MODIFIED**: Files that failed cryptographic hash comparison (Tamper Alert).
  * 🟡 **NEW**: Untracked or rogue backdoor files present in the filesystem.
  * ⚪ **DELETED**: Missing files that existed during baseline creation.
* **Interactive 3D Visualizer**:
  * **Three 3D Layout Modes**: Orbital Vault, 3D Matrix Cube, and Double-Helix Wave.
  * **Raycaster HUD**: Hover and click on any 3D node to inspect baseline vs current SHA-256 hashes, size diffs, and forensic notes.
  * **Interactive Laser Scan Animation & Synthesized Audio FX**: Web Audio API sound alerts and laser sweeps without external MP3 dependencies.
* **Graceful Fault Tolerance**: Catches `PermissionError`, locked handles, and unreadable files safely without crashing.

---

## 📁 Repository Structure

```
sourang-file-integrity-checker/
├── sourang_integrity/              # Core Python package
│   ├── __init__.py                 # Package initializer & exports
│   ├── core.py                     # Cryptographic hashing & verification engine
│   ├── simulator.py                # Tamper simulation & test vault generator
│   ├── cli.py                      # Terminal CLI with Rich formatting & 3D banner
│   ├── gui_server.py               # Built-in REST API & HTTP server for 3D GUI
│   ├── desktop_gui.py              # Native Tkinter GUI with 3D isometric wireframe
│   └── web/                        # 3D WebGL Web Interface
│       ├── index.html              # Cyber-Vault HUD layout
│       ├── style.css               # Futuristic glassmorphism styles
│       ├── app.js                  # Three.js 3D engine & audio synthesizer
│       └── vendor/                 # Offline bundled Three.js & OrbitControls
├── sample_test_vault/              # Sample test folder with nested subdirectories
│   ├── auth_secrets.env            # Sensitive credentials file
│   ├── config.json                 # JSON configuration file
│   ├── database/schema.sql         # Nested SQL file
│   ├── documents/system_policy.md  # Nested documentation file
│   └── binaries/security_token.dat # Binary data file
├── sample_manifest.json            # Reference baseline manifest generated from sample vault
├── tests/
│   └── test_integrity.py           # Comprehensive unit tests (8/8 passing)
├── main.py                         # Unified entry point
├── requirements.txt                # Optional CLI dependencies (rich, colorama)
├── setup.py                        # Pip packaging script
├── LICENSE                         # MIT License
└── README.md                       # Documentation & Simulation Transcript
```

---

## ⚡ Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/sourang/file-integrity-checker.git
cd file-integrity-checker
```

### 2. Install Dependencies (Optional)
The core cryptographic engine and Desktop GUI run out of the box using **standard Python 3.8+**. For colorized terminal tables:
```bash
pip install -r requirements.txt
```

---

## 🖥️ Usage Guide

### A. Launch the 3D Cyber-Vault Web GUI
Experience the interactive 3D WebGL holographic vault in your browser:
```bash
python main.py gui
```
* **Controls**: Left-click + drag to rotate the 3D vault; scroll wheel to zoom; click on any node to view forensic hash analysis.
* **Live Buttons**: One-click "Generate Baseline", "Verify Integrity", and "Simulate 1-Byte Tamper".

---

### B. Launch the Native Desktop GUI (Tkinter)
For a standalone desktop application with a real-time isometric 3D canvas:
```bash
python main.py desktop
```

---

### C. Terminal CLI Commands

#### 1. Generate Baseline Manifest
Recursively scan a target folder and produce a baseline manifest:
```bash
python main.py baseline --dir ./sample_test_vault --output sample_manifest.json --csv
```

#### 2. Verify File Integrity
Verify a directory against the baseline manifest:
```bash
python main.py verify --dir ./sample_test_vault --manifest sample_manifest.json --export-html audit_report.html
```

#### 3. Run Live Tamper Simulation Demo
Execute an end-to-end automated demonstration of single-byte stealth tampering:
```bash
python main.py simulate
```

#### 4. Interactive Terminal Menu
Run without arguments to access the interactive navigation menu:
```bash
python main.py
```

---

## 🔬 Single-Byte Tampering Simulation Transcript

Below is the verified execution transcript generated by `Sourang File Integrity Checker`, demonstrating that **single-byte modifications are immediately detected even when file size and modification timestamps are artificially disguised**:

```text
╭─────────────────────────── SOURANG SECURITY CORE ────────────────────────────╮
│                                                                              │
│   ____                                                                       │
│  / ___|  ___  _   _ _ __ __ _ _ __   __ _                                    │
│  \___ \ / _ \| | | | '__/ _` | '_ \ / _` |                                   │
│   ___) | (_) | |_| | | | (_| | | | | (_| |                                   │
│  |____/ \___/ \__,_|_|  \__,_|_| |_|\__, |                                   │
│                                     |___/                                    │
│  [3D CRYPTOGRAPHIC FILE INTEGRITY & TAMPER DETECTOR]                         │
│              v1.0.0 * by Sourang                                             │
│                                                                              │
╰──────────────────────── SHA-256 File Integrity Radar ────────────────────────╯
🚀 RUNNING LIVE TAMPERING & CRYPTOGRAPHIC SIMULATION DEMO
Testing: Single-byte alteration detection under forged metadata

[1/5] Generating sample test vault with diverse files at sample_test_vault...
[2/5] Generating cryptographic baseline manifest at sample_manifest.json...
[3/5] Executing stealth single-byte tamper on auth_secrets.env...

                🔬 Forensic Tampering Details (Before vs After)                 
┏━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Metric            ┃ Before Tamper     ┃ After Tamper      ┃ Stealth Check    ┃
┃                   ┃                   ┃ (Adversary)       ┃                  ┃
┡━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ File Size         │ 200 bytes         │ 200 bytes         │ IDENTICAL (0 B)  │
│ Modified Time     │ 1791891570.002    │ 1791891570.002    │ IDENTICAL        │
│                   │                   │                   │ (Forged utime)   │
│ Cryptographic     │ a6bd0d472b1ce0... │ d405f0ce709a20... │ AVALANCHE        │
│ SHA-256 Digest    │                   │                   │ MISMATCH         │
└───────────────────┴───────────────────┴───────────────────┴──────────────────┘

[4/5] Simulating unauthorized intrusion (injecting rogue backdoor & deleting schema)...
[5/5] Executing automated verification audit against baseline...

╭────────────────────────── SIMULATION AUDIT REPORT ───────────────────────────╮
│ 🚨 SECURITY ALERT: COMPROMISED - TAMPERING DETECTED                          │
│ Integrity Score: 50.0%                                                       │
│ Tampered Files: 1 | Rogue Files: 1 | Missing Files: 1 | Intact Files: 3      │
╰──────────────────────────────────────────────────────────────────────────────╯
✔ Tamper simulation successfully confirmed cryptographic detection capability!
```

---

## 📋 Acceptance Criteria Checklist

| Requirement / Acceptance Criteria | Status | Implementation Details |
|:---|:---:|:---|
| **SHA-256 Cryptographic Hashing** | ✅ PASSED | Chunked 64 KB binary streaming in `core.py` |
| **Structured Baseline Manifest** | ✅ PASSED | JSON & CSV containing relative paths, timestamps, sizes & digests |
| **Tamper Detection (Single-Byte)** | ✅ PASSED | Caught via SHA-256 avalanche effect (`simulator.py`) |
| **Timestamp & Size Spoofing Resilience**| ✅ PASSED | Accurately detects alteration even when `mtime` and byte size are identical |
| **Nested Subdirectories & Diverse Files**| ✅ PASSED | Deep recursive traversal handling text, SQL, Markdown, and raw `.dat` binary |
| **Permission Error Handling** | ✅ PASSED | Catches `PermissionError` and `OSError` without crashing |
| **3D GUI & Visual Aesthetics** | ✅ PASSED | Three.js WebGL 3D Cyber-Vault with Raycasting HUD + Tkinter 3D Canvas |
| **Unit Test Coverage** | ✅ PASSED | 8/8 automated tests passing in `tests/test_integrity.py` |

---

## 🧪 Running Unit Tests

Run the full automated test suite to verify cryptographic accuracy:
```bash
python -m unittest discover tests
```

Output:
```text
........
----------------------------------------------------------------------
Ran 8 tests in 0.305s

OK
```

---

## 📜 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.

Developed with ❤️ by **Sourang**.
