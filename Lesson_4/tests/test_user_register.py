import requests
from Lesson_4.lib.base_case import BaseCase
from Lesson_4.lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup_method(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"

    def test_user_create_successfully(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': self.email
        }

        response = requests.post("https://playground.learnqa.ru/ajax/api/user/", data=data)
        Assertions.assert_status_code(response, 200)
        # assert response.status_code == 200, f"Unexpected status code {response.status_code}"
        # print(response.content)
        Assertions.assert_json_has_key(response, "id")

    def test_create_user_with_existing_email(self):
        email = 'vinkotov@example.com'
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learnqa',
            'lastName': 'learnqa',
            'email': email
        }

        response = requests.post("https://playground.learnqa.ru/ajax/api/user/", data=data)

        print(response.status_code)
        print(response.content)

        Assertions.assert_status_code(response, 400)
        # assert response.status_code == 400, f"Unexpected status code {response.status_code}"
        assert response.content.decode("utf-8") == f"Users with email '{email}' already exists", f"Unexpected response content {repponse.content}"