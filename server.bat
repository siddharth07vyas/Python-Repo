@echo off
title Google Sheets Translation Server
echo ================================================
echo    Google Sheets Translation Web Server
echo ================================================
echo.

REM Check if virtual environment exists
if not exist "sheets" (
    echo ❌ Setup not completed!
    echo Please run 'setup.bat' first to install dependencies
    echo.
    pause
    exit /b 1
)

REM Check if credentials.json exists
if not exist "credentials.json" (
    echo ❌ credentials.json not found!
    echo Please add your Google Service Account credentials file
    echo.
    pause
    exit /b 1
)

echo ✅ Starting web server...
echo.
echo 🌐 Open your browser and go to: http://localhost:5000
echo 🛑 Press Ctrl+C to stop the server
echo.

REM Activate environment and run Flask app
call sheets\Scripts\activate.bat
python app.py