from uuid import uuid4
import pandas as pd
from datetime import datetime
import numpy as np
import pathlib


def tilfeldig_uuid(n) -> list[str]:
    return [str(uuid4()) for _ in range(n)]


def tilfeldig_datetime(n, start: datetime, end: datetime) -> list[datetime]:
    start_ts = int(start.timestamp())
    end_ts = int(end.timestamp())
    return [
        datetime.fromtimestamp(r)
        for r in np.random.uniform(
            low=start_ts,
            high=end_ts,
            size=n,
        )
    ]


def tilfeldig_kategori(n, kategorier: list[str]):
    return np.random.choice(kategorier, size=n)


def generer(n: int):
    return pd.DataFrame(
        data={
            "id": tilfeldig_uuid(n),
            "tidspunkt": tilfeldig_datetime(
                n, datetime(2023, 1, 1), datetime(2023, 5, 1)
            ),
            "kategori": tilfeldig_kategori(
                n, ["søknad", "inntektsmelding", "sykmelding", "vedtak"]
            ),
        }
    )


if __name__ == "__main__":
    mappe = pathlib.Path("data")
    mappe.mkdir(exist_ok=True, parents=True)
    df = generer(int(1e6))
    df.to_parquet(mappe / "data.parquet")
    df.to_csv(mappe / "data.csv", index=False)
