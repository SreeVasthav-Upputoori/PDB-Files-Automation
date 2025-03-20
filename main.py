import os
import requests
import pandas as pd

def download_pdb(pdb_id, save_dir):
    url = f'https://files.rcsb.org/download/{pdb_id}.pdb'
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(os.path.join(save_dir, f'{pdb_id}.pdb'), 'w') as file:
            file.write(response.text)
        print(f"Downloaded: {pdb_id}.pdb")
    else:
        print(f"Failed to download: {pdb_id}.pdb")

def find_input_file():
    for file in ["pdb_ids.csv", "pdb_ids.txt", "pdb_ids.xlsx"]:
        if os.path.exists(file):
            return file
    raise FileNotFoundError("No input file found. Ensure pdb_ids.csv, pdb_ids.txt, or pdb_ids.xlsx is present.")

def read_pdb_ids(input_file):
    ext = os.path.splitext(input_file)[1].lower()
    
    if ext == '.txt':
        with open(input_file, 'r') as file:
            return [line.strip() for line in file if line.strip()]
    elif ext == '.csv':
        df = pd.read_csv(input_file)
    elif ext in ['.xls', '.xlsx']:
        df = pd.read_excel(input_file)
    else:
        raise ValueError("Unsupported file format. Use TXT, CSV, or XLSX.")
    
    # Identify the column containing PDB IDs regardless of name
    col_name = None
    for col in df.columns:
        if "pdb" in col.lower().replace("_", "").replace(" ", ""):
            col_name = col
            break
    
    if col_name is None:
        raise ValueError("No column found containing PDB IDs. Ensure the file has a valid column.")
    
    return df[col_name].dropna().astype(str).tolist()

def download_pdb_from_file(save_dir):
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    input_file = find_input_file()
    pdb_ids = read_pdb_ids(input_file)
    
    for pdb_id in pdb_ids:
        download_pdb(pdb_id, save_dir)

if __name__ == "__main__":
    save_dir = "pdb_files"  # Directory to save PDB files
    download_pdb_from_file(save_dir)
