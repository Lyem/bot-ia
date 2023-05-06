from core.__seedwork.infra.http.contracts.http import Response, Http
from requests import get, post

class RequestsService(Http):
    
    @staticmethod
    def get(url: str, params=None, **kwargs) -> Response:
        response = get(url, params=params, **kwargs)
        return Response(response.status_code, response.text, response.content)
    
