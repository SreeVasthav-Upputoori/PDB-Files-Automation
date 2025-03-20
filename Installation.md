# Installation Guide for PDB Downloader

This guide provides step-by-step instructions to install and use the **PDB-Files-Automation** tool.

---

## **1. Clone the Repository**
First, download the project from GitHub:
```bash
git clone https://github.com/SreeVasthav-Upputoori/PDB-Files-Automation  
cd pdb_downloader
```

---

## **2. Install Dependencies**
Make sure you have **Python 3.6+** installed. Then, install the required libraries:
```bash
pip install -r requirements.txt
```

---

## **3. Install the Package (Optional)**
To install the script as a **command-line tool**, run:
```bash
python setup.py install
```

---

## **4. Prepare Your Input File**
The script accepts a **list of PDB IDs** in one of these formats:
- `pdb_ids.csv`
- `pdb_ids.txt`
- `pdb_ids.xlsx`

**Example Format (`pdb_ids.csv` or `pdb_ids.txt`):**
```
1A4G
2HIU
3M8L
4ZEO
5XDL
```

If using Excel (`.xlsx`), put the PDB IDs in the **first column**.

---

## **5. Run the Script**
After preparing your file, run:
```bash
python main.py
```

If you installed it as a package, you can also use:
```bash
pdb_downloader
```

---

## **6. Check Output**
The downloaded PDB files will be saved in the **`pdb_files/`** folder.

---

## **7. Uninstall (If Needed)**
To remove the package, run:
```bash
pip uninstall pdb_downloader
```

---

Now you’re ready to download PDB files automatically! 
