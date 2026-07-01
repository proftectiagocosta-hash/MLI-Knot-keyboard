@echo off
setlocal

cd /d "%~dp0"

if exist ".venv\Scripts\activate.bat" (
    call ".venv\Scripts\activate.bat"
)

python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
pyinstaller --noconfirm --clean --onefile --windowed --name MLI-Knot-keyboard main.py

echo.
echo Build finished. Executable:
echo dist\MLI-Knot-keyboard.exe

