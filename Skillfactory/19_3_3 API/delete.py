import requests

#Удаляем питомца метод DELETE
res = requests.delete(f'https://petstore.swagger.io/v2/pet/6578458588546', headers={'Content-type': 'application/json'})
print(res.text)