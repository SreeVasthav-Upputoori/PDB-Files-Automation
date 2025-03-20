from setuptools import setup, find_packages

setup(
    name="pdb_downloader",
    version="1.0.0",
    author="Your Name",
    author_email="sreevasthav.upputoori@gmail.com",
    description="A script to download PDB files from RCSB PDB using a list of PDB IDs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/SreeVasthav-Upputoori/PDB-Files-Automation",  
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "openpyxl"
    ],
    entry_points={
        "console_scripts": [
            "pdb_downloader=main:download_pdb_from_file"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
