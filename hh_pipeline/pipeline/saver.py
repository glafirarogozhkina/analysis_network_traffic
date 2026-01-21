from typing import Any, Tuple

import numpy as np
import pandas as pd

from pipeline.base import Handler


class SaverHandler(Handler):
    """
    Обработчик сохранения данных в .npy файлы.
    """

    def process(self, data: Any) -> None:
        """
        Сохраняет X и y в файлы x_data.npy и y_data.npy.

        :param data: кортеж (X, y)
        """
        if not isinstance(data, tuple) or len(data) != 2:
            raise TypeError("SaverHandler ожидает кортеж (X, y)")

        X, y = data

        if not isinstance(X, pd.DataFrame) or not isinstance(y, pd.Series):
            raise TypeError("SaverHandler ожидает (DataFrame, Series)")

        np.save("x_data.npy", X.to_numpy())
        np.save("y_data.npy", y.to_numpy())

