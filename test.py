


import jwt
import time


secret_key = 'secret'

payload = {'test':1122, 'lee': 'lok'}

payload['exp'] = int(time.time()) + 60

token = jwt.encode(payload, secret_key).decode()


data = jwt.decode('dsadas.dsada.dsada', secret_key, algorithms='HS256')
print(data)