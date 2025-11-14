# Google Sheets API Translation Extractor

This script extracts multilingual translations from a Google Sheet and saves them as a JSON file.

## Quick Start

### Prerequisites
- Python 3.7+ installed on your system
- Google Service Account credentials (credentials.json file)

### Setup (One-time)
1. Double-click `setup.bat` to automatically install dependencies
2. Place your `credentials.json` file in the project folder

### Running the Script
1. Double-click `run.bat`
2. The translations will be saved to `translations.json`

## Manual Setup (Alternative)

If you prefer manual setup:

```bash
# Create virtual environment
python -m venv sheets

# Activate virtual environment (Windows)
sheets\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the script
python main.py
```

## Files
- `main.py` - Main script
- `credentials.json` - Google Service Account credentials (you need to provide this)
- `requirements.txt` - Python dependencies
- `setup.bat` - One-time setup script
- `run.bat` - Script runner
- `translations.json` - Output file (created after running)

## Troubleshooting

### "Python is not installed"
- Download and install Python from https://python.org
- Make sure to check "Add Python to PATH" during installation

### "credentials.json not found"
- Get your Google Service Account credentials from Google Cloud Console
- Save the JSON file as `credentials.json` in the project folder

### "Permission denied" or script won't run
- Right-click the .bat file and select "Run as administrator"