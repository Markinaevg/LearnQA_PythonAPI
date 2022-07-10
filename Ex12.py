import requests

class Test_EX12:
    def test_headers(self):
        response = requests.get("https://playground.learnqa.ru/api/homework_header")
        headers = response.headers
        print(f"Содержимое headers: {headers}")

        assert response.status_code == 200, "Wronge response code"
        assert "x-secret-homework-header" in headers, "There field 'x-secret-homework-header' in the response"

        assert headers["x-secret-homework-header"] == "Some secret value", f'Некорректное значение Headers. Должно быть - {headers["x-secret-homework-header"]}'
        print(f'Значение "{headers["x-secret-homework-header"]}" указано верно')