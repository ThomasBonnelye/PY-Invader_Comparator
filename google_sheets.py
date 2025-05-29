import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

SHEET_NAME = "FlashInvaders Tracker"
UID_SHEET = "UIDs"
OUTPUT_SHEET = "Comparatif"

def get_gsheet_client():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("credentials/credentials.json", scope)
    return gspread.authorize(creds)

def read_uids(sheet_name=SHEET_NAME, tab_name=UID_SHEET):
    client = get_gsheet_client()
    sheet = client.open(sheet_name).worksheet(tab_name)
    uids = sheet.col_values(1)[1:]  # skip header
    return [uid.strip() for uid in uids if uid.strip()]

def write_comparatif(df, sheet_name=SHEET_NAME, tab_name=OUTPUT_SHEET):
    client = get_gsheet_client()
    try:
        worksheet = client.open(sheet_name).worksheet(tab_name)
        worksheet.clear()
    except gspread.exceptions.WorksheetNotFound:
        worksheet = client.open(sheet_name).add_worksheet(title=tab_name, rows="100", cols="20")

    data = [ ["" if pd.isna(x) else x for x in row] for row in df.reset_index().values.tolist() ]
    header = ["Invader"] + df.columns.tolist()
    worksheet.update([header] + data)
