# Ex5: Парсинг JSON
# Давайте создадим пустой Python-скрипт.
#
#
# Внутри него создадим переменную json_text. Значение этой переменной должно быть таким, как указано тут: https://gist.github.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37
#
#
# Наша задача с помощью библиотеки “json”, которую мы показывали на занятии, распарсить нашу переменную json_text и вывести текст второго сообщения с помощью функции print.
#
#
# Ответом должна быть ссылка на скрипт в вашем репозитории.


import json

# Вариант 1
json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'

obj = json.loads(json_text)
print(obj["messages"])

for item in obj["messages"]:
    print(item["message"], item["timestamp"])




# Вариант 2
# json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
#
# obj = json.loads(json_text)
# print("Получен объект с типом", type(obj))
# print("Значение объекта", obj.get("messages", "Такого ключа нет"))
# print("Тип объекта", type(obj["messages"]))
#
# for count, value in enumerate(obj["messages"]):
#     print("Получен словарь №", count + 1, " => ", type(value), value)
#
#     print("\tРаспечатаем ключ и значение словаря:", end="\n\t\t")
#     for k, v in value.items():
#         print("Ключ= ", k, ", Значение= ", v, end="\n\t\t")
#     print("---------------------------")


