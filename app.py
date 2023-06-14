import os
import re
from dotenv import load_dotenv

load_dotenv()

os.chdir(os.getenv("DOWNLOAD_PATH"))
print(os.getcwd())

for file in os.listdir():
    name, ext = os.path.splitext(file)
    new_name = re.sub(r'\W+', '-', name) + ext
    os.rename(file, new_name)
