




url = 'https://boss-uat.maycur.com/backend/enterprise/EC3JQENUCMF8TT/services'
header = {
    'Tokenid':'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJtYXljdXJfand0X3VhdF9pZCIsInN1YiI6IlVJMjEwOTAxWFMwV1NHMiIsImlhdCI6MTY5NjkxOTU3MiwiYXVkIjoiQk9TUyIsImV4cCI6MTY5NjkyNjc3Mn0.3deeWorlEirgNU341lIdSjETgeFh3BUe2RJQNnJp36U',
    'User': 'UI210901XS0WSG2'
}
import requests

res = requests.get(url,headers=header).json()
services = res['payload']

for service in services:
    id = service['id']
    url2 = 'https://boss-uat.maycur.com/backend/enterprise/EC3JQENUCMF8TT/service'
    res2 = requests.delete(url=url2, headers=header, json={'id':id})
    print(f'id:{id}, res:{res2}')
