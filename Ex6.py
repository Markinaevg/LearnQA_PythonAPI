import requests

response = requests.post(" https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)
last_response = response

count = len(response.history)

print(f"Количество редиректов - {count}")
print(f"Итоговый редирект - {last_response.url}")

