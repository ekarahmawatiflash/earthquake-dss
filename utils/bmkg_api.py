import requests
import pandas as pd

AUTOGEMPA_URL = "https://data.bmkg.go.id/DataMKG/TEWS/autogempa.json"
GEMPA_TERKINI_URL = "https://data.bmkg.go.id/DataMKG/TEWS/gempaterkini.json"
GEMPA_DIRASAKAN_URL = "https://data.bmkg.go.id/DataMKG/TEWS/gempadirasakan.json"

def get_autogempa():
    r = requests.get(AUTOGEMPA_URL, timeout=20)
    r.raise_for_status()
    data = r.json()
    return data.get("Infogempa", {}).get("gempa", {})

def get_gempa_terkini():
    r = requests.get(GEMPA_TERKINI_URL, timeout=20)
    r.raise_for_status()
    data = r.json()
    gempa = data.get("Infogempa", {}).get("gempa", [])
    return pd.DataFrame(gempa)

def get_gempa_dirasakan():
    r = requests.get(GEMPA_DIRASAKAN_URL, timeout=20)
    r.raise_for_status()
    data = r.json()
    gempa = data.get("Infogempa", {}).get("gempa", [])
    return pd.DataFrame(gempa)