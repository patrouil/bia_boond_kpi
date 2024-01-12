import calendar
import http
import logging
import time
from http.client import HTTPConnection

import jwt

class BoondAuth:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.jwt_token = {}
        return

    def clientTokenAuth(self, client_token: str, user_token: str, client_key: str) -> None:
        t = calendar.timegm(time.gmtime())
        pl = {
            "userToken": user_token,
            "clientToken": client_token,
            "time": t,
            "mode": "normal"
        }
        t= jwt.encode(pl, client_key, algorithm="HS256")
        self.jwt_token['X-Jwt-Client-Boondmanager']= t
        return

    def connection(self, host: str) -> HTTPConnection:
        conn = http.client.HTTPConnection(host)
        conn.putheader('X-Jwt-Client-Boondmanager', self.jwt_token['X-Jwt-Client-Boondmanager'])
        return conn
    @property
    def auth_headers(self)->dict:
        return self.jwt_token