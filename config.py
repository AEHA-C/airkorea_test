# config.py

# =========================
# 에어코리아 API 설정
# =========================

API_BASE_URL = "http://apis.data.go.kr"
API_ENDPOINT = "/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty"

SERVICE_KEY = "Qc8CY3xAGFKIy1H%2FdAIzBzcSYk%2B%2FnSnyKdjEn0oNqHRVV9z7LoGeqQ4MOsFIaLO7ePhFvzBvSJUzcngkmaJN0A%3D%3D"

STATION_NAMES = [
    "부산감만", "부산북항", "부산항",
    "연산동",
    "청룡동", "회동동",
    "기장읍", "용수리",
    "우동", "좌동", "재송동",
    "광안동",
    "대연동", "용호동",
    "태종대", "청학동",
    "초량동", "수정동",
    "광복동",
    "대신동",
    "장림동", "당리동",
    "대저동", "녹산동", "명지동",
    "덕포동", "학장동", "삼락동",
    "전포동",  "개금동",
    "덕천동", "화명동"
]

API_RESPONSE_ENCODING = "utf-8"
DATA_TERM = "DAILY"
API_VERSION = "1.0"
NUM_OF_ROWS = "100"
PAGE_NO = "1"

# collectedAt 생성에 사용하는 타임존 (KST 고정)
TIMEZONE = "Asia/Seoul"

# =========================
# Google Sheets 설정
# =========================

SERVICE_ACCOUNT_FILE = "service_account.json"
SPREADSHEET_ID = "1eDrzgtt3WMEmSzUUOWJONxbllwf0gD_cMqHUoFHJX1k"

# 단일 시트 append 저장 구조
SHEET_NAME = "통합"
