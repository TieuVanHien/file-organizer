@echo off

REM Create and activate the virtual environment
python -m venv myvenv
venv\Scripts\activate.bat

REM Install dependencies
pip install -r requirements.txt

