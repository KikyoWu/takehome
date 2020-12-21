from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder
from app.libs.error_code import ServerError
from datetime import datetime

#重写JSONEncoder中的default函数
class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o,'keys') and hasattr(o,'__getitem__'):
            return dict(o)
        if isinstance(o,datetime):
            return o.strftime('%Y-%m-%d %H:%M:%S')
        raise ServerError()

#Flask调用重写JSONEncoder
class Flask(_Flask):
    json_encoder = JSONEncoder



