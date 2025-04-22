from abc import ABC, abstractmethod
from datetime import date

class DateFormatterPlugin(ABC):
    @abstractmethod
    def format(self, dt: date) -> str:
        pass
