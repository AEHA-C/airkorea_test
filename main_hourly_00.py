# main_hourly_00.py

from fetch_api import fetch_all_stations_data
from google_sheets import append_rows

TARGET_SHEET_NAME = "정각"


def run():
    rows = fetch_all_stations_data()

    if not rows:
        print("저장할 데이터가 없습니다.")
        return

    print("[DEBUG] 저장 대상:", TARGET_SHEET_NAME)
    for row in rows:
        print(row)

    result = append_rows(rows, TARGET_SHEET_NAME)
    print("구글 스프레드시트 저장 완료")
    print(result)


if __name__ == "__main__":
    run()