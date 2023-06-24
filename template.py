import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

project = "textsummarize"

list_of_files = [
    "github/workflow/.gitkeep", #for deployments
    f"src/{project}/__init__.py", #
    f"src/{project}/components/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/utils/common.py",
    f"src/{project}/logging/__init__.py",
    f"src/{project}/config/__init__.py",
    f"src/{project}/config/configration.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/constants/__init__.py",
    "config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)

    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Created directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Created empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")
