"""
Creates file structure for the project. Execute once after cloning the repository.
"""

import os
from pathlib import Path
import logging


# Logging string, the info level information.
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# List of files to be created
list_of_files = [
   'src/__init__.py',
   'src/helper.py',
   'src/prompt.py',
   '.env',
   "setup.py",
   "research/experiments.ipynb",
   "app.py",
   "store_index.py",
   "static/.gitkeep",
   "templates/chat.html",
]

# Creates the file structure
for filepath in list_of_files:
    # Convert the filepaths into Path objects, because of the OS slash issues.
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            pass
            logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"File {filename} already exists")
