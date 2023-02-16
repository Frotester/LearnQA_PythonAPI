# Ex11: Тест запроса на метод cookie
# Необходимо написать тест, который делает запрос на метод: https://playground.learnqa.ru/api/homework_cookie
# Этот метод возвращает какую-то cookie с каким-то значением. Необходимо с помощью функции print() понять что за cookie и с каким значением, и зафиксировать это поведение с помощью assert
# Чтобы pytest не игнорировал print() необходимо использовать ключик "-s": python -m pytest -s my_test.py
# =================================================
# Результатом должна быть ссылка на коммит с тестом.


# Запускать так:
# python -m pytest -s Lesson_3/test_ex11.py

import requests
from Lesson_3.lib.base_case import BaseCase

class TestEx11(BaseCase):
    def test_homework_cookie(self):
        response = requests.post("https://playground.learnqa.ru/api/homework_cookie")

        print("Выведу на печать инфо из 'dict(response.cookies)' =>", dict(response.cookies))

        # Вариант1
        assert "HomeWork" in response.cookies, "There is no cookie in the response"
        expected_value = "hw_value"
        received_value = response.cookies.get("HomeWork")
        assert received_value == expected_value, f"Received cookie '{received_value}' does not match expected value {expected_value}"

        # Вариант2 (с помощью функции (метода) из пронаследованного класса BaseCase)
        # expected_value = "hw_value"
        # received_value = self.get_cookie(response, "HomeWork")
        # assert received_value == expected_value, f"Received cookie '{received_value}' does not match expected value {expected_value}"
