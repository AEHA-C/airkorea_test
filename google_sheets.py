# google_sheets.py

from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

from config import SERVICE_ACCOUNT_FILE, SPREADSHEET_ID, SHEET_NAME

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def get_sheets_service():
    credentials = Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE,
        scopes=SCOPES,
    )
    service = build("sheets", "v4", credentials=credentials)
    return service


def append_rows(rows):
    if not rows:
        print("추가할 데이터가 없습니다.")
        return None

    service = get_sheets_service()
    sheet_range = f"{SHEET_NAME}!A:F"

    body = {"values": rows}

    result = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=SPREADSHEET_ID,
            range=sheet_range,
            valueInputOption="USER_ENTERED",
            insertDataOption="INSERT_ROWS",
            body=body,
        )
        .execute()
    )

    return result
