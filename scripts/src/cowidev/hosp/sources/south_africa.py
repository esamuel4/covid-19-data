import pandas as pd

METADATA = {
    "source_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRGCkIwakQ5rpfXky9FZhDwr3qUgerfhBLSzn9OsA79yQ_2G_y-_Ns9JjRJZWXD5kxJ3qicoL7bHGjE/pub?gid=1044172863&single=true&output=csv",
    "source_url_ref": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRGCkIwakQ5rpfXky9FZhDwr3qUgerfhBLSzn9OsA79yQ_2G_y-_Ns9JjRJZWXD5kxJ3qicoL7bHGjE/pub?gid=1044172863&single=true",
    "source_name": "",
    "entity": "South Africa",
}


def main() -> pd.DataFrame:
    df = pd.read_csv(METADATA["source_url"], usecols=["Week ending:", "National"])

    df = df.assign(indicator="Weekly new hospital admissions").rename(
        columns={
            "Week ending:": "date",
            "National": "value",
        }
    )

    df["date"] = pd.to_datetime(df.date, dayfirst=True).dt.date.astype(str)
    df["entity"] = METADATA["entity"]

    return df, METADATA
