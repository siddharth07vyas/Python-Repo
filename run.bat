@echo off
title Google Sheets Translation Extractor
echo ================================================
echo    Google Sheets Translation Extractor
echo ================================================
echo.

REM Check if virtual environment exists
if not exist "sheets" (
    echo ❌ Setup not completed!
    echo Please double-click 'setup.bat' first
    echo.
    pause
    exit /b 1
)

REM Check if credentials.json exists
if not exist "credentials.json" (
    echo ❌ credentials.json not found!
    echo.
    echo Please follow these steps:
    echo 1. Go to console.cloud.google.com
    echo 2. Create a service account
    echo 3. Download the JSON credentials file
    echo 4. Rename it to 'credentials.json'
    echo 5. Put it in this folder
    echo.
    pause
    exit /b 1
)

echo ✅ Starting translation extraction...
echo.

REM Activate environment and run script
call sheets\Scripts\activate.bat
python main.py

echo.
echo ================================================
echo ✅ SUCCESS! Translations saved to 'translations.json'
echo ================================================
echo.
echo You can now open 'translations.json' to see your data
echo.
pause