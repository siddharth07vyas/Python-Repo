# Google Sheets Translation Extractor

## 📋 What This Does
This tool extracts translations from your Google Sheet and saves them as a JSON file.

## 🚀 Quick Start (3 Steps)

### Step 1: Get Google Credentials (One Time Setup)
1. Go to [Google Cloud Console](https://console.cloud.google.com)
2. Click "Create Project" → Enter any name → Click "Create"
3. In the search bar, type "Google Sheets API" → Click on it → Click "Enable"
4. Go to "Credentials" (left menu) → Click "Create Credentials" → "Service Account"
5. Enter any name → Click "Create" → Skip optional steps → Click "Done"
6. Click on the service account you just created
7. Go to "Keys" tab → "Add Key" → "Create New Key" → "JSON" → Download
8. Rename the downloaded file to `credentials.json`
9. Put `credentials.json` in the same folder as these files

### Step 2: One-Time Setup
1. **Double-click `setup.bat`**
2. Wait for it to finish (may take a few minutes)

### Step 3: Run the Tool
1. **Double-click `run.bat`**
2. Your translations will be saved as `translations.json`

## 📁 Files You Need
- `main.py` - The main program
- `requirements.txt` - List of required components
- `setup.bat` - One-click setup
- `run.bat` - One-click runner
- `credentials.json` - Your Google credentials (you create this)

## ❓ Troubleshooting

**"Python not found"**
- Download Python from [python.org](https://python.org)
- During installation, check "Add Python to PATH"

**"credentials.json not found"**
- Make sure the credentials file is named exactly `credentials.json`
- Make sure it's in the same folder as the other files

**"Permission denied"**
- Right-click the .bat file and select "Run as administrator"

## 🎯 That's It!
The tool will create a `translations.json` file with all your translations organized by language.