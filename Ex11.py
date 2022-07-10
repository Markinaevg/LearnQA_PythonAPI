import requests

class Test_EX11:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies
        print(f"Содержимое cookie: {cookie}")
        assert cookie["HomeWork"] == "hw_value", "Некорректное значение Cookie"