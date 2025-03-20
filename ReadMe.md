with open("README.md", "w") as f:
    f.write("""# PDB File Downloader

This script downloads PDB files from the RCSB PDB website based on a list of PDB IDs provided in CSV, TXT, or XLSX format.

## Features
- Automatically detects input file (CSV > TXT > XLSX)
- Downloads PDB files from RCSB PDB
- Saves files in a specified directory

## Installation
```bash
pip install requests pandas openpyxl
