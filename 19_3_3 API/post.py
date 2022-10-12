import requests
import json

data = {
  "id": 6578458588546,
  "category": {
    "id": 457874548,
    "name": "pokemon"
  },
  "name": "Bulbazavr",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "pok"
    }
  ],
  "status": "available"
}
#Создаем питомца. Метод POST
res = requests.post(f'https://petstore.swagger.io/v2/pet', headers={'Content-type': 'application/json'}, data=json.dumps(data))

print(res.text)
