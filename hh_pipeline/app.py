import sys

from pipeline.reader import ReaderHandler
from pipeline.cleaner import CleanerHandler
from pipeline.encoder import EncoderHandler
from pipeline.splitter import SplitterHandler
from pipeline.saver import SaverHandler


def main() -> None:
    """
    Точка входа в приложение.
    """
    if len(sys.argv) != 2:
        raise ValueError("Использование: python app.py path/to/file.csv")

    csv_path = sys.argv[1]

    # Создаём обработчики
    reader = ReaderHandler()
    cleaner = CleanerHandler()
    encoder = EncoderHandler()
    splitter = SplitterHandler()
    saver = SaverHandler()

    # Собираем цепочку
    reader.set_next(cleaner)\
          .set_next(encoder)\
          .set_next(splitter)\
          .set_next(saver)

    # Запускаем пайплайн
    reader.handle(csv_path)


if __name__ == "__main__":
    main()

