from abc import ABC, abstractmethod

class GreetingPlugin(ABC):
    @abstractmethod
    def greet(self, name: str) -> str:
        pass
