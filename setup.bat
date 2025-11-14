@echo off
echo Setting up Google Sheets API project...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed or not in PATH!
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "sheets" (
    echo Creating virtual environment...
    python -m venv sheets
)

REM Activate virtual environment and install dependencies
echo Activating virtual environment and installing dependencies...
call sheets\Scripts\activate.bat
pip install -r requirements.txt

echo.
echo Setup complete! 
echo.
echo To run the script:
echo 1. Make sure credentials.json is in the project folder
echo 2. Run: run.bat
echo.
pause