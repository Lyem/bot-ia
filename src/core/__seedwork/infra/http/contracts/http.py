from abc import ABC, abstractmethod
import json

class Response:
    def __init__(self, status: int, data: str, content):
        self.status = status
        self.data = data
        self.content = content
    
    def json(self):
        return json.loads(self.data)

class Http(ABC):

    @abstractmethod
    def get(url: str, params=None, **kwargs) -> Response:
        raise NotImplementedError()
    
