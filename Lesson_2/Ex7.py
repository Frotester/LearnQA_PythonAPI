# Ex7: Запросы и методы
#
# Сегодня задача должна быть попроще. У нас есть вот такой URL: https://playground.learnqa.ru/ajax/api/compare_query_type
#
#
# Запрашивать его можно четырьмя разными HTTP-методами: POST, GET, PUT, DELETE
#
#
# При этом в запросе должен быть параметр method. Он должен содержать указание метода, с помощью которого вы делаете запрос. Например, если вы делаете GET-запрос, параметр method должен равняться строке ‘GET’. Если POST-запросом - то параметр method должен равняться ‘POST’.  И так далее.
#
#
# Надо написать скрипт, который делает следующее:
#
#
# 1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.
#
#
# 2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.
#
#
# 3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.
#
#
# 4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.
#
#
# Не забывайте, что для GET-запроса данные надо передавать через params=
#
# А для всех остальных через data=
#
#
# Итогом должна быть ссылка на коммит со скриптом и ответы на все 4 вопроса.


import requests

print("1. Делает http-запрос любого типа без параметра method, описать что будет выводиться в этом случае.")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.text)


print("2. Делает http-запрос не из списка. Например, HEAD. Описать что будет выводиться в этом случае.")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "HEAD"})
print(response.text)


print("3. Делает запрос с правильным значением method. Описать что будет выводиться в этом случае.")
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": "GET"})
print(response.text)

response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": "POST"})
print(response.text)


print("4. С помощью цикла проверяет все возможные сочетания реальных типов запроса и значений параметра method. Например с GET-запросом передает значения параметра method равное ‘GET’, затем ‘POST’, ‘PUT’, ‘DELETE’ и так далее. И так для всех типов запроса. Найти такое сочетание, когда реальный тип запроса не совпадает со значением параметра, но сервер отвечает так, словно все ок. Или же наоборот, когда типы совпадают, но сервер считает, что это не так.")
lst = ['GET', 'POST', 'PUT', 'DELETE']

def my_call(message, func):
    lst = ['GET', 'POST', 'PUT', 'DELETE']
    print(message)
    for el in lst:
        print("\tс параметром method:", el)
        if func == requests.get:
            response = func("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method": el})
        else:
            response = func("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method": el})
        print("\t\tОтвет:", response.text)

my_call("Вызов метода GET:", requests.get)
my_call("Вызов метода POST:", requests.post)
my_call("Вызов метода PUT:", requests.put)
my_call("Вызов метода DELETE:", requests.delete)
