import re

import pandas as pd


IT_KEYWORDS = [
    "developer", "разработчик", "программист", "software",
    "backend", "frontend", "fullstack",
    "python", "java", "javascript", "js",
    "data scientist", "data engineer",
    "machine learning", "ml",
    "c++", "c#", "php", "go",
]

EXCLUDE_KEYWORDS = [
    "manager", "менеджер",
    "руководитель", "project", "product",
    "pm", "hr", "recruiter",
]


def filter_it_roles(df: pd.DataFrame) -> pd.DataFrame:
    """
    Оставляет только резюме IT-разработчиков по названию должности.
    """
    title = df["Ищет работу на должность:"].str.lower()

    include_pattern = "|".join(IT_KEYWORDS)
    exclude_pattern = "|".join(EXCLUDE_KEYWORDS)

    include_mask = title.str.contains(include_pattern, regex=True, na=False)
    exclude_mask = title.str.contains(exclude_pattern, regex=True, na=False)

    return df[include_mask & ~exclude_mask].reset_index(drop=True)


def parse_experience(text: str) -> float | None:
    """
    Извлекает количество лет опыта из текста.
    """
    if not isinstance(text, str):
        return None

    match = re.search(r"(\d+)\s*(?:год|лет)", text.lower())
    if match:
        return float(match.group(1))

    return None


def define_level(row: pd.Series) -> str | None:
    """
    Определяет уровень специалиста: junior / middle / senior.
    """
    title = str(row["Ищет работу на должность:"]).lower()
    exp_text = row["Опыт (двойное нажатие для полной версии)"]

    if "junior" in title:
        return "junior"
    if "middle" in title:
        return "middle"
    if "senior" in title:
        return "senior"

    years = parse_experience(exp_text)

    if years is None:
        return None
    if years < 2:
        return "junior"
    if years < 5:
        return "middle"
    return "senior"
