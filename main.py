from fetch_api import fetch_all_stations_data
from google_sheets import append_rows

RUN_TYPE = "정각"


def run():
    rows = fetch_all_stations_data(RUN_TYPE)

    if not rows:
        print("저장할 데이터가 없습니다.")
        return

    append_rows(rows)

    print("구글 스프레드시트 저장 완료")
    print(rows)


if __name__ == "__main__":
    run()
