@echo off
echo ================================================
echo  Google Sheets Translation Extractor
echo ================================================
echo.
echo Checking Python installation...
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

echo Python found! Checking dependencies...

REM Install dependencies if needed
pip install -r requirements.txt >nul 2>&1

echo Running translation extractor...
echo.

REM Run the standalone script
python script.py

echo.
echo Script execution completed.
pause