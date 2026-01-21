from typing import Any

import pandas as pd

from pipeline.base import Handler


class CleanerHandler(Handler):
    """
    Обработчик очистки данных.
    """

    def process(self, data: Any) -> pd.DataFrame:
        """
        Очищает DataFrame от пустых строк и столбцов.

        :param data: pandas.DataFrame
        :return: очищенный pandas.DataFrame
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError("CleanerHandler ожидает pandas.DataFrame")

        df = data.copy()

        # Удаляем полностью пустые строки
        df = df.dropna(how="all")

        # Удаляем полностью пустые столбцы
        df = df.dropna(axis=1, how="all")

        # Сбрасываем индекс
        df = df.reset_index(drop=True)

        return df

