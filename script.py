"""
Google Sheets Translation Extractor - Standalone Version
========================================================

A simple command-line tool to extract translations from Google Sheets.
No browser required - just run and get your JSON file!

Usage: python standalone_extractor.py
"""

import gspread
from google.oauth2.service_account import Credentials
import json
import os
from datetime import datetime
import sys

def extract_translations():
    """
    Extract translations from Google Sheets
    Returns: (translations_dict, error_message)
    """
    try:
        print("🔐 Authenticating with Google Sheets API...")
        
        # Define required scopes for Google Sheets access
        scopes = ['https://www.googleapis.com/auth/spreadsheets']

        # Try to authenticate using credentials.json file
        if not os.path.exists('credentials.json'):
            return None, "❌ credentials.json file not found! Please add your Google Service Account credentials."
        
        # Load credentials and authorize client
        creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
        client = gspread.authorize(creds)
        print("✅ Authentication successful!")

        print("📊 Accessing Google Sheet...")
        
        # Your Google Sheet ID (extracted from the URL)
        sheet_id = "1ylU7pHpN6iEy1v5Q5pDTg9Kr5_uzLsx4rPKKZrmRFmY"
        sheet = client.open_by_key(sheet_id)
        worksheet = sheet.sheet1
        
        print("📋 Reading sheet data...")
        
        # Get all translation keys (first column, excluding header)
        multilang_key = list(worksheet.col_values(1))
        multilang_key = [key.strip() for key in multilang_key if key.strip()]
        multilang_key = list(multilang_key)
        multilang_key.pop(0)  # Remove header row


        # Get all language columns (header row, excluding first column and Slovak)
        header_cols = worksheet.row_values(1)
        header_cols = [col.strip() for col in header_cols if col.strip()]
        
        # Remove Slovak and first column (keys column)
        if "Slovak" in header_cols:
            header_cols.remove("Slovak")
        header_cols = header_cols[1:]  # Exclude first column (keys)
        
        print(f"🌐 Found languages: {', '.join(header_cols)}")
        
        # Extract translations for each language
        translation_key_values = {}
        
        print("\n🔄 Processing translations...")
        for i, language in enumerate(header_cols):
            print(f"   📖 Processing {language}... ({i+1}/{len(header_cols)})")
            
            # Find column index for this language
            language_cell = worksheet.find(language)
            if language_cell:
                key_index = language_cell.col
                
                # Get all values from this language column
                key_col_values = worksheet.col_values(key_index)
                key_col_values = [cell.strip() for cell in key_col_values if cell.strip()]
                
                # Create dictionary mapping keys to translations
                # Skip header row [1:] and match with translation keys
                key_value_multilang = dict(zip(multilang_key, key_col_values[1:]))
                translation_key_values[language] = key_value_multilang

        # Add metadata
        translation_key_values["_metadata"] = {
            "generated_at": datetime.now().isoformat(),
            "total_keys": len(multilang_key),
            "languages": header_cols,
            "generated_by": "Google Sheets Translation Extractor"
        }

        print("✅ Translation extraction completed!")
        return translation_key_values, None
        
    except gspread.exceptions.SpreadsheetNotFound:
        return None, "❌ Google Sheet not found! Please check the sheet ID and permissions."
    except gspread.exceptions.APIError as e:
        return None, f"❌ Google API Error: {str(e)}"
    except FileNotFoundError:
        return None, "❌ credentials.json file not found! Please add your Google Service Account credentials."
    except json.JSONDecodeError:
        return None, "❌ Invalid credentials.json file! Please check the file format."
    except Exception as e:
        return None, f"❌ Unexpected error: {str(e)}"

def save_translations(translations):
    """
    Save translations to JSON file in current directory
    Returns: (filename, error_message)
    """
    try:
        # Create filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"translations_{timestamp}.json"
        
        print(f"💾 Saving translations to {filename}...")
        
        # Save to current directory
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=4)
        
        # Get file size for confirmation
        file_size = os.path.getsize(filename)
        file_size_kb = round(file_size / 1024, 2)
        
        print(f"✅ File saved successfully!")

        
        return filename, None
        
    except PermissionError:
        return None, "❌ Permission denied! Cannot write to current directory."
    except Exception as e:
        return None, f"❌ Error saving file: {str(e)}"

# def print_summary(translations, filename):
#     """Print extraction summary"""
#     print("\n" + "=" * 60)
#     print("📋 EXTRACTION SUMMARY")
#     print("=" * 60)
    
#     metadata = translations.get("_metadata", {})
#     total_keys = metadata.get("total_keys", 0)
#     languages = metadata.get("languages", [])
    
#     print(f"📝 Total translation keys: {total_keys}")
#     print(f"🌐 Languages extracted: {len(languages)}")
#     print(f"📅 Generated at: {metadata.get('generated_at', 'Unknown')}")
#     print(f"💾 Saved as: {filename}")
#     print(f"📁 Full path: {os.path.abspath(filename)}")
    
#     print("\n🌍 Available languages:")
#     for lang in languages:
#         key_count = len(translations.get(lang, {}))
#         print(f"   • {lang}: {key_count} translations")
    
#     print("\n✅ Extraction completed successfully!")
#     print("🎉 You can now use the JSON file in your application!")

def main():
    """Main function to run the extraction process"""
    try:        
        # Extract translations from Google Sheets
        translations, error = extract_translations()
        
        if error:
            print(f"\n{error}")
            input("\nPress Enter to exit...")
            return
        
        # Save translations to JSON file
        filename, save_error = save_translations(translations)
        
        if save_error:
            print(f"\n{save_error}")
            input("\nPress Enter to exit...")
            return
        
        # # Print summary
        # print_summary(translations, filename)
        
        print("\n" + "=" * 60)
        input("Press Enter to exit...")
        
    except KeyboardInterrupt:
        print("\n\n❌ Process interrupted by user")
        print("👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {str(e)}")
        input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()