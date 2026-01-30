import sys

from pipeline.reader import ReaderHandler
from pipeline.cleaner import CleanerHandler
from pipeline.encoder import EncoderHandler
from pipeline.splitter import SplitterHandler
from pipeline.saver import SaverHandler
from pipeline.salary_parser import SalaryParserHandler



def main() -> None:
    """
    Точка входа в приложение.
    """
    if len(sys.argv) != 2:
        raise ValueError("Использование: python app.py path/to/file.csv")

    csv_path = sys.argv[1]

    # создаём обработчики
    reader = ReaderHandler()
    cleaner = CleanerHandler()
    salary_parser = SalaryParserHandler()
    splitter = SplitterHandler()
    encoder = EncoderHandler()
    saver = SaverHandler()

    # собираем цепочку
    reader.set_next(cleaner)
    cleaner.set_next(salary_parser)
    salary_parser.set_next(splitter)
    splitter.set_next(encoder)
    encoder.set_next(saver)

    # Запускаем пайплайн
    reader.handle(csv_path)


if __name__ == "__main__":
    main()

