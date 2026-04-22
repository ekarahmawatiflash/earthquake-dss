import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    confusion_matrix,
    classification_report
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from xgboost import XGBClassifier

from utils.data_processing import FEATURE_COLS, TARGET_COL, LABEL_MAP

def build_pipeline() -> Pipeline:
    preprocessor = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), FEATURE_COLS)
    ])

    model = XGBClassifier(
        n_estimators=300,
        max_depth=6,
        learning_rate=0.05,
        objective="multi:softprob",
        num_class=3,
        eval_metric="mlogloss",
        random_state=42,
        n_jobs=-1,
    )

    return Pipeline([
        ("pre", preprocessor),
        ("model", model),
    ])

def train_and_evaluate(df: pd.DataFrame):
    df_train = df.dropna(subset=[TARGET_COL]).copy()

    X = df_train[FEATURE_COLS]
    y = df_train[TARGET_COL].astype(int)

    stratify_value = y if y.nunique() > 1 else None

    try:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42, stratify=stratify_value
        )
    except ValueError:
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision, recall, f1, _ = precision_recall_fscore_support(
        y_test, y_pred, average="weighted", zero_division=0
    )
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1, 2])

    report = classification_report(
        y_test,
        y_pred,
        labels=[0, 1, 2],
        target_names=["Minor", "Moderate", "Severe"],
        zero_division=0,
        output_dict=True
    )

    report_df = pd.DataFrame(report).transpose()

    return pipeline, {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "confusion_matrix": cm,
        "report_df": report_df
    }

def predict_all(pipeline: Pipeline, df: pd.DataFrame):
    out = df.copy()
    out["pred_damage"] = pipeline.predict(df[FEATURE_COLS])
    out["pred_label"] = out["pred_damage"].map(LABEL_MAP)
    return out

def get_feature_importance(pipeline: Pipeline):
    model = pipeline.named_steps["model"]
    importances = model.feature_importances_

    return pd.DataFrame({
        "feature": FEATURE_COLS,
        "importance": importances
    }).sort_values("importance", ascending=False)