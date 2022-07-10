import requests

class Test_EX11:
    def test_cookie(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_cookie")
        cookie = response.cookies
        print(f"Содержимое cookie: {cookie}")

        assert response.status_code == 200, "Wronge response code"
        assert "HomeWork" in cookie, "There field 'HomeWork' in the response"

        assert cookie["HomeWork"] == "hw_value", "Некорректное значение Cookie"

