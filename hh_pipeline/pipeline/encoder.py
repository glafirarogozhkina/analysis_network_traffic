from typing import Any, Tuple

import pandas as pd

from pipeline.base import Handler


class EncoderHandler(Handler):
    """
    Обработчик кодирования категориальных признаков.
    Кодирует ТОЛЬКО X, y передаёт дальше без изменений.
    """

    def process(self, data: Any) -> Tuple[pd.DataFrame, pd.Series]:
        # ожидаем кортеж (X, y)
        if not isinstance(data, tuple) or len(data) != 2:
            raise TypeError("EncoderHandler ожидает кортеж (X, y)")

        X, y = data

        if not isinstance(X, pd.DataFrame):
            raise TypeError("EncoderHandler ожидает X как pandas.DataFrame")

        df = X.copy()

        # One-hot encoding для категориальных признаков
        df = pd.get_dummies(df, drop_first=True)

        return df, y
