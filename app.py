from flask import Flask, render_template, send_file, request, jsonify
import gspread
from google.oauth2.service_account import Credentials
import json
import os
from datetime import datetime

app = Flask(__name__)

def extract_translations():
    """Extract translations from Google Sheets"""
    try:
        scopes = [
            'https://www.googleapis.com/auth/spreadsheets'
        ]

        # Try to use environment variable first (for cloud deployment)
        credentials_json = os.getenv('GOOGLE_CREDENTIALS')
        if credentials_json:
            # Parse credentials from environment variable
            credentials_info = json.loads(credentials_json)
            creds = Credentials.from_service_account_info(credentials_info, scopes=scopes)
        else:
            # Fallback to file (for local development)
            creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
        client = gspread.authorize(creds)

        sheet_id = "1ylU7pHpN6iEy1v5Q5pDTg9Kr5_uzLsx4rPKKZrmRFmY"
        sheet = client.open_by_key(sheet_id)

        worksheet = sheet.sheet1
        multilang_key = list(worksheet.col_values(1))
        multilang_key = [key.strip() for key in multilang_key if key.strip()]
        
        # Get column indices
        eng_cell_index = worksheet.find("Value").col
        german_cell_index = worksheet.find("German").col
        hindi_cell_index = worksheet.find("Hindi").col
        french_cell_index = worksheet.find("French").col
        portuguese_cell_index = worksheet.find("Portugese").col
        spanish_cell_index = worksheet.find("Spanish").col
        rassian_cell_index = worksheet.find("Russian").col
        italian_cell_index = worksheet.find("Italian").col
        dutch_cell_index = worksheet.find("Dutch").col
        chinese_cell_index = worksheet.find("Chinese(PRC)").col
        japanese_cell_index = worksheet.find("Japanese").col

        # Get column values
        eng_cell_values = worksheet.col_values(eng_cell_index)
        german_cell_values = worksheet.col_values(german_cell_index)
        hindi_cell_values = worksheet.col_values(hindi_cell_index)
        french_cell_values = worksheet.col_values(french_cell_index)
        portuguese_cell_values = worksheet.col_values(portuguese_cell_index)
        spanish_cell_values = worksheet.col_values(spanish_cell_index)
        rassian_cell_values = worksheet.col_values(rassian_cell_index)
        italian_cell_values = worksheet.col_values(italian_cell_index)
        dutch_cell_values = worksheet.col_values(dutch_cell_index)
        chinese_cell_values = worksheet.col_values(chinese_cell_index)
        japanese_cell_values = worksheet.col_values(japanese_cell_index)

        # Clean values
        eng_cell_values = [cell.strip() for cell in eng_cell_values if cell.strip()]
        german_cell_values = [cell.strip() for cell in german_cell_values if cell.strip()]
        hindi_cell_values = [cell.strip() for cell in hindi_cell_values if cell.strip()]
        french_cell_values = [cell.strip() for cell in french_cell_values if cell.strip()]
        portuguese_cell_values = [cell.strip() for cell in portuguese_cell_values if cell.strip()]
        spanish_cell_values = [cell.strip() for cell in spanish_cell_values if cell.strip()]
        rassian_cell_values = [cell.strip() for cell in rassian_cell_values if cell.strip()]
        italian_cell_values = [cell.strip() for cell in italian_cell_values if cell.strip()]
        dutch_cell_values = [cell.strip() for cell in dutch_cell_values if cell.strip()]
        chinese_cell_values = [cell.strip() for cell in chinese_cell_values if cell.strip()]
        japanese_cell_values = [cell.strip() for cell in japanese_cell_values if cell.strip()]

        # Create translations dictionaries
        translation_en = {}
        translation_gn = {}
        translation_hi = {}
        traslation_fr = {}
        translation_pt = {}
        translation_sk = {}
        translation_es = {}
        translation_ru = {}
        translation_it = {}
        translation_nl = {}
        translation_cn = {}
        translation_jp = {}

        for i, key in enumerate(multilang_key):
            translation_en[key] = eng_cell_values[i] if i < len(eng_cell_values) else ""
            translation_gn[key] = german_cell_values[i] if i < len(german_cell_values) else ""
            translation_hi[key] = hindi_cell_values[i] if i < len(hindi_cell_values) else ""
            traslation_fr[key] = french_cell_values[i] if i < len(french_cell_values) else ""
            translation_pt[key] = portuguese_cell_values[i] if i < len(portuguese_cell_values) else ""
            translation_es[key] = spanish_cell_values[i] if i < len(spanish_cell_values) else ""
            translation_ru[key] = rassian_cell_values[i] if i < len(rassian_cell_values) else ""
            translation_it[key] = italian_cell_values[i] if i < len(italian_cell_values) else ""
            translation_nl[key] = dutch_cell_values[i] if i < len(dutch_cell_values) else ""
            translation_cn[key] = chinese_cell_values[i] if i < len(chinese_cell_values) else ""
            translation_jp[key] = japanese_cell_values[i] if i < len(japanese_cell_values) else ""

        # Create final translations object
        translations = {
            "English": translation_en,
            "German": translation_gn,
            "Hindi": translation_hi,
            "French": traslation_fr,
            "Portuguese": translation_pt,
            "Slovak": translation_sk,
            "Spanish": translation_es,
            "Russian": translation_ru,
            "Italian": translation_it,
            "Dutch": translation_nl,
            "Chinese": translation_cn,
            "Japanese": translation_jp,
            "generated_at": datetime.now().isoformat(),
            "total_keys": len(multilang_key)
        }

        return translations, None
        
    except Exception as e:
        return None, str(e)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    try:
        translations, error = extract_translations()
        
        if error:
            return jsonify({
                "success": False,
                "error": error,
            }), 500
        
        # Save to file
        filename = f"translations_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        filepath = os.path.join('downloads', filename)
        
        # Create downloads directory if it doesn't exist
        os.makedirs('downloads', exist_ok=True)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(translations, f, ensure_ascii=False, indent=4)
        
        return jsonify({
            "success": True,
            "message": "Translations extracted successfully!",
            "download_url": f"/download/{filename}",
            "data": translations
        })
        
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

@app.route('/download/<filename>')
def download_file(filename):
    filepath = os.path.join('downloads', filename)
    if os.path.exists(filepath):
        return send_file(filepath, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    # For production deployment (Vercel, Heroku, etc.)
    app.debug = False