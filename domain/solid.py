from abc import ABC, abstractmethod

class Solid(ABC):
    @abstractmethod
    def volume(self) -> float:
        pass
