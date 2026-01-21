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

        :param data: pandas.DataFrame
        :return: (X, y)
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("SplitterHandler ожидает pandas.DataFrame")

        if data.shape[1] < 2:
            raise ValueError("Недостаточно столбцов для разделения X и y")

        df = data.copy()

        # Последний столбец считаем целевой переменной
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]

        return X, y

