# Ex12: Тест запроса на метод header
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_header
# Этот метод возвращает headers с каким-то значением. Необходимо с помощью функции print() понять что за headers и с каким значением, и зафиксировать это поведение с помощью assert
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
#
# =============================================================
# Результатом должна быть ссылка на коммит с тестом.
#


# Запускать так:
# python -m pytest -s Lesson_3/test_ex12.py

import requests
from Lesson_3.lib.base_case import BaseCase

class TestEx12(BaseCase):
    def test_homework_cookie(self):
        response = requests.post("https://playground.learnqa.ru/api/homework_header")

        print("Выведу на печать инфо из 'dict(response.cookies)' =>", dict(response.headers))

        # Вариант1
        assert "x-secret-homework-header" in response.headers, "There is no header in the response"
        expected_value = "Some secret value"
        received_value = response.headers.get("x-secret-homework-header")
        assert received_value == expected_value, f"Received cookie '{received_value}' does not match expected value {expected_value}"

        # Вариант2
        # expected_value = "Some secret value"
        # received_value = self.get_header(response, "x-secret-homework-header")
        # assert received_value == expected_value, f"Received cookie '{received_value}' does not match expected value {expected_value}"

