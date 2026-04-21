# config.py

# =========================
# 에어코리아 API 설정
# =========================

API_BASE_URL = "http://apis.data.go.kr"
API_ENDPOINT = "/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"

SERVICE_KEY = "Qc8CY3xAGFKIy1H%2FdAIzBzcSYk%2B%2FnSnyKdjEn0oNqHRVV9z7LoGeqQ4MOsFIaLO7ePhFvzBvSJUzcngkmaJN0A%3D%3D"

STATION_NAMES = [
    "부산감만",
    "부산북항",
    "부산항",
    "연산동",
    "청룡동",
    "기장읍",
    "우동",
    "광안동",
    "당리동",
    "대저동",
    "덕포동",
    "전포동"
]

API_RESPONSE_ENCODING = "utf-8"
DATA_TERM = "DAILY"
API_VERSION = "1.0"
NUM_OF_ROWS = "100"
PAGE_NO = "1"

TIMEZONE = "Asia/Seoul"

# =========================
# Google Sheets 설정
# =========================

SERVICE_ACCOUNT_FILE = "service_account.json"
SPREADSHEET_ID = "1eDrzgtt3WMEmSzUUOWJONxbllwf0gD_cMqHUoFHJX1k"

SHEET_NAME = "정각"
SHEET_RANGE = f"{SHEET_NAME}!A:E"
