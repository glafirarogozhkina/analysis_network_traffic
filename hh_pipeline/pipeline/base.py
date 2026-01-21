from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    Абстрактный базовый класс обработчика
    для паттерна Chain of Responsibility.
    """

    def __init__(self) -> None:
        self._next_handler: Optional["Handler"] = None

    def set_next(self, handler: "Handler") -> "Handler":
        """
        Устанавливает следующий обработчик в цепочке.
        """
        self._next_handler = handler
        return handler

    def handle(self, data: Any) -> Any:
        """
        Обрабатывает данные и передаёт результат дальше по цепочке.
        """
        result = self.process(data)

        if self._next_handler is not None:
            return self._next_handler.handle(result)

        return result

    @abstractmethod
    def process(self, data: Any) -> Any:
        """
        Основная логика обработки данных.
        """
        pass
