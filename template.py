import os
from pathlib import Path
import logging

logging.basicConfig(Level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "TextSummarizer"

list_of_files = [
    ".github/workFlow/.gitkeep",
    f"src/{projrct_name}/__init__.py",
    f"src/{projrct_name}/components/__init__.py",
    f"src/{projrct_name}/utils/__init__.py",
    f"src/{projrct_name}/utils/common.py",
    f"src/{projrct_name}/logging//__init__.py",
    f"src/{projrct_name}/config/__init__.py",
    f"src/{projrct_name}/config/configuration.py",
    f"src/{projrct_name}/pipeline/configuration.py",
    f"src/{projrct_name}/entity/__init__.py",
    f"src/{projrct_name}/constants/__init__.py",
    "config/congfing.yaml",
    "params.yaml",
    "app.yaml",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.jpynb",

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename= os.pah.split(filepath)

    if filedie != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating Directory:{filedir} for the file {filename} ")

    if(not os.path.exist(ilepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating mpty file: {filepath}")
