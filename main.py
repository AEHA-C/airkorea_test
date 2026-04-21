from fetch_api import fetch_all_stations_data
from google_sheets import append_rows

HEADER = ["dataTime", "stationName", "pm10Value", "pm25Value"]

def run():
    rows = fetch_all_stations_data()

    if not rows:
        print("저장할 데이터가 없습니다.")
        return

    # 👉 처음 실행 시 헤더 추가 (선택)
    # append_rows([HEADER])

    append_rows(rows)

    print("구글 스프레드시트 저장 완료")
    print(rows)


if __name__ == "__main__":
    run()