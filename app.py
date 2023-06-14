import os
import re
from dotenv import load_dotenv
import shutil

load_dotenv()

os.chdir(os.getenv("DOWNLOAD_PATH"))

# create folders
if not os.path.exists("images"):
    os.mkdir("images")
if not os.path.exists("docs"):
    os.mkdir("docs")
if not os.path.exists("video"):
    os.mkdir("video")
if not os.path.exists("others"):
    os.mkdir("others")        

# refactor files
for file in os.listdir():
    if os.path.isfile(file):
        name, ext = os.path.splitext(file)
        new_name = re.sub(r'\W+', '-', name) + ext
        os.rename(file, new_name)
    else:
        continue #ignore subfolders
    if ext.lower() in ['.jpg', '.png', '.gif']:
        shutil.move(file, "images")
    elif ext.lower() in ['.mov', '.mp4', '.mkv', '.webm']:
        shutil.move(file, "video")
    elif ext.lower() in ['.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.pdf', '.txt', '.csv', '.rtf']:
        shutil.move(file, "docs")
    else:
        shutil.move(file, "others")        