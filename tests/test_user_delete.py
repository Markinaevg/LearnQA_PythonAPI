from lib.my_requests import MyRequests
from lib.base_case import BaseCase
from lib.assertions import Assertions
import allure

@allure.epic("User delete cases")
class TestUserDelete(BaseCase):
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

    def test_delete_id_2_user(self):
        login_response = MyRequests.post(
                "/user/login/",
                data={
                    'email': 'vinkotov@example.com',
                    'password': '1234',
                }
            )

        auth_sid = self.get_cookie(login_response, "auth_sid")
        token = self.get_header(login_response, "x-csrf-token")
        user_id = self.get_json_value(login_response, "user_id")

        delete_response = MyRequests.delete(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
            )

        Assertions.assert_code_status(delete_response, 400)
        assert delete_response.text == "Please, do not delete test users with ID 1, 2, 3, 4 or 5."

    def test_create_and_delete_user(self):
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

        auth_sid = self.get_cookie(login_response, "auth_sid")
        token = self.get_header(login_response, "x-csrf-token")
        user_id = self.get_json_value(login_response, "user_id")

        delete_response = MyRequests.delete(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
            )

        Assertions.assert_code_status(register_response, 200)
        assert delete_response.text == ""

        get_response = MyRequests.get(
                f"/user/{user_id}",
                headers={"x-csrf-token": token},
                cookies={"auth_sid": auth_sid},
            )

        Assertions.assert_code_status(register_response, 200)
        assert get_response.text == "User not found"

    def test_delete_other_user(self):
        register_data = self.prepare_registration_date()
        register_response = MyRequests.post("/user/", data=register_data)
        Assertions.assert_code_status(register_response, 200)
        Assertions.assert_json_has_key(register_response, "id")

        user_id = self.get_json_value(register_response, "id")

        register_data_2 = self.prepare_registration_date()
        register_response_2 = MyRequests.post("/user/", data=register_data_2)
        Assertions.assert_code_status(register_response_2, 200)
        Assertions.assert_json_has_key(register_response_2, "id")

        login_response_2 = MyRequests.post(
            "/user/login/",
            data={
                "email": register_data_2["email"],
                "password": register_data_2["password"],
            },
            )

        auth_sid_2 = self.get_cookie(login_response_2, "auth_sid")
        token_2 = self.get_header(login_response_2, "x-csrf-token")

        delete_response = MyRequests.delete(
            f"/user/{user_id}",
            headers={"x-csrf-token": token_2},
            cookies={"auth_sid": auth_sid_2},
        )

        Assertions.assert_code_status(delete_response, 200)
        assert delete_response.text == ""
