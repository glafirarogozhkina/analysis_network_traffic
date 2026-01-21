import pandas as pd
from typing import Any

from pipeline.base import Handler


class ReaderHandler(Handler):
    """
    Обработчик чтения CSV-файла.
    """

    def __init__(self, nrows: int = 10_000) -> None:
        super().__init__()
        self.nrows = nrows

    def process(self, data: Any) -> Any:
        if not isinstance(data, str):
            raise TypeError("ReaderHandler ожидает путь к CSV-файлу")

        df = pd.read_csv(data, nrows=self.nrows)
        return df
