import re
from typing import Any

import pandas as pd

from pipeline.base import Handler


class SalaryParserHandler(Handler):
    """
    Преобразует колонку 'ЗП' в числовой формат (рубли).
    """

    def process(self, data: Any) -> pd.DataFrame:
        if not isinstance(data, pd.DataFrame):
            raise TypeError("SalaryParserHandler ожидает pandas.DataFrame")

        df = data.copy()

        def parse_salary(value: str) -> float:
            if not isinstance(value, str):
                return float("nan")

            value = value.replace("\xa0", " ")

            match = re.search(r"(\d+)", value)
            if not match:
                return float("nan")

            salary = float(match.group(1))
            salary *= 1000  # приводим к рублям

            return salary

        df["ЗП"] = df["ЗП"].apply(parse_salary)

        return df

