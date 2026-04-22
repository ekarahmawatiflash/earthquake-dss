import pandas as pd

def compute_priority_score(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()

    damage_score_map = {
        "Minor": 1,
        "Moderate": 2,
        "Severe": 3
    }

    out["damage_score"] = out["pred_label"].map(damage_score_map).fillna(0)
    out["hazard_score"] = out["zona_kerentanan_enc"].fillna(0)
    out["slope_score"] = out["lereng_topografi_enc"].fillna(0)
    out["soil_score"] = out["lokasi_tanah_enc"].fillna(0)

    out["distance_score"] = out["jarak_km"].apply(
        lambda x: 3 if pd.notna(x) and x < 10 else (2 if pd.notna(x) and x < 20 else 1)
    )

    out["priority_score"] = (
        0.35 * out["damage_score"] +
        0.25 * out["hazard_score"] +
        0.15 * out["slope_score"] +
        0.10 * out["soil_score"] +
        0.15 * out["distance_score"]
    )

    def label_priority(score):
        if score >= 2.4:
            return "High Priority"
        elif score >= 1.6:
            return "Medium Priority"
        return "Low Priority"

    out["priority_label"] = out["priority_score"].apply(label_priority)
    return out