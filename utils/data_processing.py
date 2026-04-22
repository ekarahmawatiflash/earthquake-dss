import re
from typing import Optional, Tuple
import numpy as np
import pandas as pd

FEATURE_COLS = [
    "jarak_km",
    "elevasi_lt_200m",
    "elevasi_200_500m",
    "elevasi_500_1500m",
    "elevasi_1500_3000m",
    "elevasi_gt_3000m",
    "mengungsi_enc",
    "lereng_topografi_enc",
    "status_daerah_enc",
    "lokasi_tanah_enc",
    "zona_kerentanan_enc",
    "lat",
    "lon",
]

TARGET_COL = "kerusakan_outcome_enc"
COORD_COL = "titik_koordinat"

LABEL_MAP = {
    0: "Minor",
    1: "Moderate",
    2: "Severe",
}

def dms_to_decimal(deg, minute, sec, hemi):
    dec = float(deg) + float(minute) / 60 + float(sec) / 3600
    if str(hemi).upper() in ["S", "W"]:
        dec *= -1
    return dec

def parse_dms_pair(text: str) -> Tuple[Optional[float], Optional[float]]:
    pattern = re.compile(
        r"(\d+)°(\d+)[′'](\d+)[″\"]([NS])\s+(\d+)°(\d+)[′'](\d+)[″\"]([EW])"
    )
    match = pattern.search(str(text))
    if not match:
        return None, None

    lat = dms_to_decimal(*match.groups()[0:4])
    lon = dms_to_decimal(*match.groups()[4:8])
    return lat, lon

def prepare_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    lat_list, lon_list = [], []
    for val in df[COORD_COL]:
        lat, lon = parse_dms_pair(val)
        lat_list.append(lat)
        lon_list.append(lon)

    df["lat"] = lat_list
    df["lon"] = lon_list

    df = df.replace([np.inf, -np.inf], np.nan)

    for col in FEATURE_COLS + [TARGET_COL]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df

def check_required_columns(df: pd.DataFrame):
    required_cols = [COORD_COL] + [c for c in FEATURE_COLS if c not in ["lat", "lon"]] + [TARGET_COL]
    return [c for c in required_cols if c not in df.columns]