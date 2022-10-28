import requests
import json


status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/findByStatus?status={status}", headers={'accept': 'application/json'})
# Запрос GET, получаем питомцев по статусу
print(res.text)
print()


