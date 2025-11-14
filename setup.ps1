# PowerShell setup script
Write-Host "Setting up Google Sheets API project..." -ForegroundColor Green

# Check if Python is installed
try {
    $pythonVersion = python --version 2>$null
    Write-Host "Found Python: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "Python is not installed or not in PATH!" -ForegroundColor Red
    Write-Host "Please install Python from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Create virtual environment if it doesn't exist
if (-not (Test-Path "sheets")) {
    Write-Host "Creating virtual environment..." -ForegroundColor Yellow
    python -m venv sheets
}

# Activate virtual environment and install dependencies
Write-Host "Installing dependencies..." -ForegroundColor Yellow
& .\sheets\Scripts\Activate.ps1
pip install -r requirements.txt

Write-Host "`nSetup complete!" -ForegroundColor Green
Write-Host "To run the script:" -ForegroundColor Cyan
Write-Host "1. Make sure credentials.json is in the project folder" -ForegroundColor White
Write-Host "2. Run: .\run.ps1" -ForegroundColor White
Read-Host "`nPress Enter to continue"