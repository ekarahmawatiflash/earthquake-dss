import pandas as pd

def safe_int(v):
    try:
        if v is None or pd.isna(v):
            return None
        return int(float(v))
    except Exception:
        return None

def rr_recommendation(pred_damage, zona, lereng, tanah):
    if pred_damage == 0:
        return "Monitoring / Light rehabilitation"

    if pred_damage == 1:
        return "Structural rehabilitation (limited reinforcement)"

    notes = []
    if zona == 3:
        notes.append("High vulnerability zone")
    if lereng == 1:
        notes.append("Steep slope")
    if tanah in [1, 2]:
        notes.append("Unstable soil")

    base = "Total reconstruction / Relocation"
    return base + (" | " + ", ".join(notes) if notes else "")

def add_rr_recommendation(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["RR_recommendation"] = out.apply(
        lambda r: rr_recommendation(
            int(r["pred_damage"]),
            safe_int(r["zona_kerentanan_enc"]),
            safe_int(r["lereng_topografi_enc"]),
            safe_int(r["lokasi_tanah_enc"]),
        ),
        axis=1,
    )
    return out