@echo off
set "venv_dir=venv"

if not exist "%venv_dir%" (
    echo Creating virtual environment...
    python -m venv "%venv_dir%"
    echo Activating virtual environment...
    call ".\%venv_dir%\Scripts\activate.bat"
    echo Installing PySide6...
    pip install PySide6
    echo Installing openpyxl
    pip install openpyxl
) else (
    echo Activating virtual environment...
    call ".\%venv_dir%\Scripts\activate.bat"
)

echo Running main.py...
pythonw main.py
