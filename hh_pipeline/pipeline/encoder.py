from typing import Any

import pandas as pd

from pipeline.base import Handler


class EncoderHandler(Handler):
    """
    Обработчик кодирования категориальных признаков.
    """

    def process(self, data: Any) -> pd.DataFrame:
        """
        Кодирует категориальные признаки в числовой вид.

        :param data: pandas.DataFrame
        :return: pandas.DataFrame с числовыми признаками
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("EncoderHandler ожидает pandas.DataFrame")

        df = data.copy()

        # One-hot encoding для категориальных признаков
        df = pd.get_dummies(df, drop_first=True)

        return df

