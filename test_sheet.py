from google_sheets import get_sheets_service
from config import SPREADSHEET_ID

service = get_sheets_service()

try:
    result = service.spreadsheets().get(
        spreadsheetId=SPREADSHEET_ID
    ).execute()

    print("성공:", result["properties"]["title"])

except Exception as e:
    print("에러:", e)