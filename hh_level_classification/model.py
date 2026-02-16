import re

import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def parse_salary(text: str) -> float | None:
    if not isinstance(text, str):
        return None

    match = re.search(r"(\d+)", text.replace(" ", ""))
    if match:
        return float(match.group(1)) * 1000

    return None


def parse_age(text: str) -> float | None:
    if not isinstance(text, str):
        return None

    match = re.search(r"(\d+)\s*year", text.lower())
    if match:
        return float(match.group(1))

    return None


def parse_experience(text: str) -> float | None:
    if not isinstance(text, str):
        return None

    match = re.search(r"(\d+)\s*(?:год|лет)", text.lower())
    if match:
        return float(match.group(1))

    return None


def train_and_evaluate(df: pd.DataFrame) -> None:
    df["salary"] = df["ЗП"].apply(parse_salary)
    df["age"] = df["Пол, возраст"].apply(parse_age)
    df["experience"] = df["Опыт (двойное нажатие для полной версии)"].apply(
        parse_experience
    )

    features = df[["salary", "age", "experience"]]
    features = features.fillna(features.median())

    X = features
    y = df["level"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced",
    )
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    print(classification_report(y_test, y_pred))


if __name__ == "__main__":
    from preprocessing import filter_it_roles, define_level

    data = pd.read_csv("../hh_pipeline/data/hh.csv")

    it_df = filter_it_roles(data)
    it_df["level"] = it_df.apply(define_level, axis=1)
    it_df = it_df.dropna(subset=["level"])

    train_and_evaluate(it_df)

