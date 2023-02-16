# Ex10: Тест на короткую фразу
# В рамках этой задачи с помощью pytest необходимо написать тест, который просит ввести в консоли любую фразу короче 15 символов. А затем с помощью assert проверяет, что фраза действительно короче 15 символов.
# Чтобы в переменную получить значение, введенное из консоли, необходимо написать вот такой код:
# phrase = input("Set a phrase: ")
# Внимание, чтобы pytest не игнорировал команду ввода с клавиатуры, запускать тест нужно с ключиком "-s": python -m pytest -s my_test.py
# =========================================
# Результатом должна стать ссылка на такой тест.


# Запускать так:
# python -m pytest -s Lesson_3/test_ex10.py

class TestEx10:

    def test_phrase_len(self):
        phrase = input("ATTENTION!!!! Set a phrase: ")
        assert len(phrase) < 15, f"Your phrase '{phrase}' is longer or equal than 15 characters long: {len(phrase)}"
