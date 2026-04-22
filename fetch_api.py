# fetch_api.py

import requests
from urllib.parse import quote
from datetime import datetime
from zoneinfo import ZoneInfo

from config import (
    API_BASE_URL,
    API_ENDPOINT,
    SERVICE_KEY,
    STATION_NAMES,
    API_RESPONSE_ENCODING,
    DATA_TERM,
    API_VERSION,
    NUM_OF_ROWS,
    PAGE_NO,
    TIMEZONE,
)


def build_request_url(station_name: str) -> str:
    encoded_station_name = quote(station_name)

    url = (
        f"{API_BASE_URL}{API_ENDPOINT}"
        f"?serviceKey={SERVICE_KEY}"
        f"&returnType=json"
        f"&numOfRows={NUM_OF_ROWS}"
        f"&pageNo={PAGE_NO}"
        f"&stationName={encoded_station_name}"
        f"&dataTerm={DATA_TERM}"
        f"&ver={API_VERSION}"
    )
    return url


def fetch_station_data(station_name: str):
    url = build_request_url(station_name)
    print(f"[DEBUG] 요청 URL: {url}")

    response = requests.get(url, timeout=30)
    response.raise_for_status()
    response.encoding = API_RESPONSE_ENCODING

    data = response.json()

    response_root = data.get("response", {})
    header = response_root.get("header", {})
    body = response_root.get("body", {})
    items = body.get("items", [])

    result_code = header.get("resultCode")
    result_msg = header.get("resultMsg")

    if result_code != "00":
        raise ValueError(f"{station_name} 조회 실패: {result_code} / {result_msg}")

    if not items:
        return None

    latest = items[0]

    # dataTime은 API 원본 문자열을 그대로 사용한다.
    row = [
        latest.get("dataTime", ""),
        latest.get("stationName", station_name),
        latest.get("pm10Value", ""),
        latest.get("pm25Value", ""),
    ]

    return row


def fetch_all_stations_data(run_type: str):
    rows = []

    # 실행 시각은 KST로 고정한다.
    collected_at = datetime.now(ZoneInfo(TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")

    for station_name in STATION_NAMES:
        try:
            station_row = fetch_station_data(station_name)

            if station_row:
                row = [run_type, collected_at] + station_row
                rows.append(row)
            else:
                print(f"[INFO] {station_name}: 데이터 없음")

        except Exception as e:
            print(f"[ERROR] {station_name}: {e}")

    return rows
