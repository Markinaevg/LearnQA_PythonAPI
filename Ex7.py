import requests

#1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Задание 1")
print("URL - ", response.url)
print("Содержание ответа - ", response.text)
print("Код ответа - ", response.status_code)


#2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
response_new = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print("Задание 2")
print("URL - ", response_new.url)
print("Содержимое ответа - ", response_new.text)
print("Код ответа", response_new.status_code)


#3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
payload = {"method":"GET"}
response_new2 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=payload)
print("Задание 3")
print("URL - ", response_new2.url)
print("Содержимое ответа - ", response_new2.text)
print("Код ответа", response_new2.status_code)

#4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method.
# Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее.
# И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра,
# но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.

print("Задание 4")
url = "https://playground.learnqa.ru/ajax/api/compare_query_type"
method = ["GET", "POST", "PUT", "DELETE"]

for i in method:
    payload3 = {"method": i}
    response1 = requests.get(url, params=payload3)
    response2 = requests.post(url, data=payload3)
    response3 = requests.put(url, data=payload3)
    response4 = requests.delete(url, data=payload3)
    if (i != "GET" and response1.text != "Wrong method provided") or (i == "GET" and response1.status_code != 200):
        print(f"Метод GET с параметром {i} возращает ответ - ", response1.text)
        print("Код ответа - ", response1.status_code)
    if (i != "POST" and response2.text != "Wrong method provided") or (i == "POST" and response2.status_code != 200):
        print(f"Метод POST с параметром {i} возращает ответ - ", response2.text)
        print("Код ответа - ", response2.status_code)
    if (i != "PUT" and response3.text != "Wrong method provided") or (i == "PUT" and response3.status_code != 200):
        print(f"Метод PUT с параметром {i} возращает ответ - ", response3.text)
        print("Код ответа - ", response3.status_code)
    if (i != "DELETE" and response4.text != "Wrong method provided") or (i == "GET" and response4.status_code != 200):
        print(f"Метод DELETE с параметром {i} возращает ответ - ", response4.text)
        print("Код ответа - ", response4.status_code)
