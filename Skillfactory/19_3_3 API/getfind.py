import requests

status = 'available'
res = requests.get(f"https://petstore.swagger.io/v2/pet/6578458588546", headers={'accept': 'application/json'})
# Запрос GET, получаем питомца по ID
print(res.text)
