import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets'
]

creds = Credentials.from_service_account_file('credentials.json', scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1ylU7pHpN6iEy1v5Q5pDTg9Kr5_uzLsx4rPKKZrmRFmY"
sheet = client.open_by_key(sheet_id)

worksheet = sheet.sheet1
multilang_key = list(worksheet.col_values(1))  # Example: Get the value of cell A1
multilang_key = [key.strip() for key in multilang_key if key.strip()]
eng_cell_index = worksheet.find("Value").col
german_cell_index = worksheet.find("German").col
hindi_cell_index = worksheet.find("Hindi").col
french_cell_index = worksheet.find("French").col
portuguese_cell_index = worksheet.find("Portugese").col
##slovak_cell_index = worksheet.find("Slovak").col
spanish_cell_index = worksheet.find("Spanish").col
rassian_cell_index = worksheet.find("Russian").col
italian_cell_index = worksheet.find("Italian").col
dutch_cell_index = worksheet.find("Dutch").col
chinese_cell_index = worksheet.find("Chinese(PRC)").col
japanese_cell_index = worksheet.find("Japanese").col

eng_cell_values = worksheet.col_values(eng_cell_index)
german_cell_values = worksheet.col_values(german_cell_index)
hindi_cell_values = worksheet.col_values(hindi_cell_index)
french_cell_values = worksheet.col_values(french_cell_index)
portuguese_cell_values = worksheet.col_values(portuguese_cell_index)
##slovak_cell_values = worksheet.col_values(slovak_cell_index)
spanish_cell_values = worksheet.col_values(spanish_cell_index)
rassian_cell_values = worksheet.col_values(rassian_cell_index)
italian_cell_values = worksheet.col_values(italian_cell_index)
dutch_cell_values = worksheet.col_values(dutch_cell_index)
chinese_cell_values = worksheet.col_values(chinese_cell_index)
japanese_cell_values = worksheet.col_values(japanese_cell_index)


# Clean the eng_cell values by removing newlines and extra whitespace
eng_cell_values = [cell.strip() for cell in eng_cell_values if cell.strip()]
## skip blank cells
eng_cell_values = [cell for cell in eng_cell_values if cell]
german_cell_values = [cell.strip() for cell in german_cell_values if cell.strip()]
hindi_cell_values = [cell.strip() for cell in hindi_cell_values if cell.strip()]
french_cell_values = [cell.strip() for cell in french_cell_values if cell.strip()]
portuguese_cell_values = [cell.strip() for cell in portuguese_cell_values if cell.strip()]
##slovak_cell_values = [cell.strip() for cell in slovak_cell_values if cell.strip()]
spanish_cell_values = [cell.strip() for cell in spanish_cell_values if cell.strip()]
rassian_cell_values = [cell.strip() for cell in rassian_cell_values if cell.strip()]
italian_cell_values = [cell.strip() for cell in italian_cell_values if cell.strip()]
dutch_cell_values = [cell.strip() for cell in dutch_cell_values if cell.strip()]
chinese_cell_values = [cell.strip() for cell in chinese_cell_values if cell.strip()]
japanese_cell_values = [cell.strip() for cell in japanese_cell_values if cell.strip()]

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
    ##translation_sk[key] = slovak_cell_values[i] if i < len(slovak_cell_values) else ""
    translation_es[key] = spanish_cell_values[i] if i < len(spanish_cell_values) else ""
    translation_ru[key] = rassian_cell_values[i] if i < len(rassian_cell_values) else ""
    translation_it[key] = italian_cell_values[i] if i < len(italian_cell_values) else ""
    translation_nl[key] = dutch_cell_values[i] if i < len(dutch_cell_values) else ""
    translation_cn[key] = chinese_cell_values[i] if i < len(chinese_cell_values) else ""
    translation_jp[key] = japanese_cell_values[i] if i < len(japanese_cell_values) else ""


# print("English Translations:", translation_en)
print("Extracting translations and saving to JSON file...")

#download in system as json file
import json
with open('translations.json', 'w', encoding='utf-8') as f:
    json.dump({
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
        "Japanese": translation_jp
    }, f, ensure_ascii=False, indent=4)

print("✅ Translations successfully saved to 'translations.json'")