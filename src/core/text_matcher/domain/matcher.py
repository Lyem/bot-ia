from abc import ABC
import abc

class IMatcher(ABC):

    @abc.abstractmethod
    def execute(self, text: str) -> int:
        raise NotImplementedError()