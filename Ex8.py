import requests
import json
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"
response = requests.get(url)
token = json.loads(response.text)["token"]
token_false = "1234566879708"
pause = json.loads(response.text)["seconds"]
print(f"Токен - {token}, Количество секунд, через сколько задача будет выполнена - {pause}")
payload = {"token": {token}}
payload2 = {"token": {token_false}}

response2 = requests.get(url, params=payload)
status2 = json.loads(response2.text)["status"]

print("Тест 1")
if status2 == "Job is NOT ready":
    print(f"Корректный ответ сервера - Задание не выполнено. Статус - {status2}")
else:
    print(f"Некорректный ответ сервера - Задание не выполнено. Статус  - {status2}")
print(f"Ответ: {response2.text}")

print("Тест 2")

time.sleep(pause)
response3 = requests.get(url, params=payload)
status3 = json.loads(response3.text)["status"]

if status3 == "Job is ready":
    print(f"Корректный ответ сервера - Задание выполнено. Статус - {status3}, пауза {pause} секунд")
else:
    print(f"Некорректный ответ сервера - Задание выполнено. Статус - {status3}, пауза {pause} секунд")
print(f"Ответ: {response3.text}")

print("Тест 3")
response4 = requests.get(url, params=payload2)

if json.loads(response4.text)["error"] != "No job linked to this token":
    print(f"Корректный ответ сервера - токен неверный - ", json.loads(response4.text)["error"])
else:
    print(f"Некорректный ответ сервера - токен неверный - ", json.loads(response4.text)["error"])
print(f"Ответ: {response4.text}")
