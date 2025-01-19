import gspread
from oauth2client.service_account import ServiceAccountCredentials

def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("Climbing Tracker").sheet1
    return sheet

def get_all_climbs():
    sheet = get_google_sheet()
    records = sheet.get_all_records()  # Fetch all records as a list of dictionaries
    return records
