# Ex13: User Agent
#
# User Agent - это один из заголовков, позволяющий серверу узнавать, с какого девайса и браузера пришел запрос.
# Он формируется автоматически клиентом, например браузером. Определив, с какого девайса или браузера пришел к нам пользователь мы сможем отдать ему только тот контент, который ему нужен.
# Наш разработчик написал метод: https://playground.learnqa.ru/ajax/api/user_agent_check
# Метод определяет по строке заголовка User Agent следующие параметры:
# device - iOS или Android
# browser - Chrome, Firefox или другой браузер
# platform - мобильное приложение или веб
# Если метод не может определить какой-то из параметров, он выставляет значение Unknown.
# Наша задача написать параметризированный тест.
# Этот тест должен брать из дата-провайдера User Agent и ожидаемые значения, GET-делать запрос с этим User Agent и убеждаться, что результат работы нашего метода правильный - т.е. в ответе ожидаемое значение всех трех полей.
# Список User Agent и ожидаемых значений можно найти по этой ссылке: https://gist.github.com/KotovVitaliy/138894aa5b6fa442163561b5db6e2e26
# Пример того, как должен выглядеть запрос с указанным User Agent:
# requests.get(
#    "https://playground.learnqa.ru/ajax/api/user_agent_check",
#     headers={"User-Agent": "Some value here"}
# )
#
# ============================================================
# На самом деле метод не всегда работает правильно. Ответом к задаче должен быть список из тех User Agent, которые вернули неправильным хотя бы один параметр, с указанием того, какой именно параметр неправильный.
# И, конечно, ссылка на коммит с вашим тестом.
#

# Запускать так:
#  python -m pytest -s Lesson_3/test_ex13.py

import requests
import pytest
import json

class TestEx13:
    # Составлю на базе инфы отсюда
    user_agents = [
        ("Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30", "Mobile", "No", "Android"),
        ("Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1", "Mobile", "Chrome", "iOS"),
        ("Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)", "Googlebot", "Unknown", "Unknown"),
        ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0", "Web", "Chrome", "No"),
        ("Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1", "Mobile", "No", "iPhone"),
    ]

    @pytest.mark.parametrize('user_agent', user_agents)
    def test_hello_call(self, user_agent):
        response = requests.get(
            "https://playground.learnqa.ru/ajax/api/user_agent_check",
            headers={"User-Agent": user_agent[0]}
        )

        # print(dict(response.json()))

        print(f"Выполнение теста для значения {user_agent[0]}")

        try:
            response_as_dict = response.json()
        except json.JSONDecodeError:
            assert False, f"Response is not in JSON format. Response text is '{response.text}'"

        assert "platform" in response_as_dict, f"Response JSON doesn't have key 'platform'"
        assert response_as_dict["platform"] == user_agent[1], f"Platform in the response '{response_as_dict['platform']}' is not equal to expected value '{user_agent[1]}'"

        assert "browser" in response_as_dict, f"Response JSON doesn't have key 'browser'"
        assert response_as_dict["browser"] == user_agent[2], f"Browser in the response '{response_as_dict['browser']}' is not equal to expected value '{user_agent[2]}'"

        assert "device" in response_as_dict, f"Response JSON doesn't have key 'device'"
        assert response_as_dict["device"] == user_agent[3], f"Device '{response_as_dict['device']}' in the response is not equal to expected '{user_agent[3]}'"


