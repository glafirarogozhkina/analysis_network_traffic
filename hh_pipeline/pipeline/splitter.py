from typing import Any, Tuple

import pandas as pd

from pipeline.base import Handler


class SplitterHandler(Handler):
    """
    Обработчик разделения данных на X и y.
    """

    def process(self, data: Any) -> Tuple[pd.DataFrame, pd.Series]:
        """
        Делит DataFrame на признаки и целевую переменную.
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("SplitterHandler ожидает pandas.DataFrame")

        if "ЗП" not in data.columns:
            raise ValueError("В данных отсутствует колонка 'ЗП'")

        df = data.copy()

        y = df["ЗП"]
        X = df.drop(columns=["ЗП"])

        return X, y
