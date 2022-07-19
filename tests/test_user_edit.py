from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("User editing cases")
class TestUserEdit(BaseCase):
    def test_edit_just_created_user(self):
       #REGISTER
        register_data = self.prepare_registration_date()
        response1 = MyRequests.post("/user/", data=register_data)

        Assertions.assert_code_status(response1, 200)
        Assertions.assert_json_has_key(response1, "id")

        email = register_data["email"]
        first_name = register_data["firstName"]
        password = register_data["password"]
        user_id = self.get_json_value(response1, "id")

       #LOGIN
        login_data = {
            'email': email,
            'password': password
        }
        response2 = MyRequests.post("/user/login", data=login_data)

        auth_sid = self.get_cookie(response2, "auth_sid")
        token = self.get_header(response2, "x-csrf-token")

        #EDIT
        new_name = "Change Name"

        response3 = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )

        with allure.step("Запрос отправлен, посмотрим код ответа"):
            Assertions.assert_code_status(response3, 200)

       #GET
        response4 = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
        )

        Assertions.assert_json_value_by_name(
           response4,
           "firstName",
           new_name,
           "Wrong name of the user after edit"
        )


#Ex 17

    def setup(self):
        register_data = self.prepare_registration_date()
        register_response = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(register_response, 200)
        Assertions.assert_json_has_key(register_response, "id")

        login_response = MyRequests.post(
            "/user/login/",
            data={
                "email": register_data["email"],
                "password": register_data["password"],
            },
        )

        self.auth_sid = self.get_cookie(login_response, "auth_sid")
        self.token = self.get_header(login_response, "x-csrf-token")
        self.user_id_from_auth_method = self.get_json_value(login_response, "user_id")

    def test_edit_without_auth(self):
        response = MyRequests.put(
            f"/user/{self.user_id_from_auth_method}",
            data={"firstName": "Other Name"},
        )
        Assertions.assert_code_status(response, 400)
        assert response.text == 'Auth token not supplied'

    def test_edit_invalid_user_email(self):
        response = MyRequests.put(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"email": "lanamail.ru"},
        )
        Assertions.assert_code_status(response, 400)
        assert response.text == "Invalid email format"

    def test_edit_user_short_firstname(self):
        response = MyRequests.put(
            f"/user/{self.user_id_from_auth_method}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"firstName": "o"},
        )
        Assertions.assert_code_status(response, 400)
        assert response.json() == {"error": "Too short value for field firstName"}

    def test_edit_other_user(self):
        response = MyRequests.put(
            f"/user/1",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
            data={"firstName": "New Name"},
        )
        Assertions.assert_code_status(response, 200)
        assert response.content.decode("utf-8") == '', f"You managed to change the user data. " \
                                                       f"Content = {response.content}"

        response2 = MyRequests.get(
            f'/user/1',
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid},
        )

        Assertions.assert_json_value_by_name(response2, "username", "Lana", "You managed to change the user data.")


