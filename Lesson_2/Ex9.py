# Ex9: Подбор пароля
# Сегодня к нам пришел наш коллега и сказал, что забыл свой пароль от важного сервиса. Он просит нас помочь ему написать программу, которая подберет его пароль.
#
#
# Условие следующее. Есть метод: https://playground.learnqa.ru/ajax/api/get_secret_password_homework
#
#
# Его необходимо вызывать POST-запросом с двумя параметрами: login и password
#
#
# Если вызвать метод без поля login или указать несуществующий login, метод вернет 500
#
#
# Если login указан и существует, метод вернет нам авторизационную cookie с названием auth_cookie и каким-то значением.
#
#
# У метода существует защита от перебора. Если верно указано поле login, но передан неправильный password, то авторизационная cookie все равно вернется. НО с "неправильным" значением, которое на самом деле не позволит создавать авторизованные запросы. Только если и login, и password указаны верно, вернется cookie с "правильным" значением. Таким образом используя только метод get_secret_password_homework невозможно узнать, передали ли мы верный пароль или нет.
#
#
# По этой причине нам потребуется второй метод, который проверяет правильность нашей авторизованной cookie: https://playground.learnqa.ru/ajax/api/check_auth_cookie
#
#
# Если вызвать его без cookie с именем auth_cookie или с cookie, у которой выставлено "неправильное" значение, метод вернет фразу "You are NOT authorized".
#
# Если значение cookie “правильное”, метод вернет: “You are authorized”
#
#
# Коллега говорит, что точно помнит свой login - это значение super_admin
#
#
# А вот пароль забыл, но точно помнит, что выбрал его из списка самых популярных паролей на Википедии (вот тебе и супер админ...).
#
#
# Ссылка: https://en.wikipedia.org/wiki/List_of_the_most_common_passwords
#
#
# Искать его нужно среди списка Top 25 most common passwords by year according to SplashData
#
#
# Итак, наша задача - написать скрипт и указать в нем login нашего коллеги и все пароли из Википедии в виде списка. Программа должна делать следующее:
#
#
# 1. Брать очередной пароль и вместе с логином коллеги вызывать первый метод get_secret_password_homework. В ответ метод будет возвращать авторизационную cookie с именем auth_cookie и каким-то значением.
#
#
# 2. Далее эту cookie мы должна передать во второй метод check_auth_cookie. Если в ответ вернулась фраза "You are NOT authorized", значит пароль неправильный. В этом случае берем следующий пароль и все заново. Если же вернулась другая фраза - нужно, чтобы программа вывела верный пароль и эту фразу.
#
#
# Ответом к задаче должен быть верный пароль и ссылка на коммит со скриптом.
#

passwords = {'!@#$%^&*',
 '000000',
 '111111',
 '121212',
 '123123',
 '1234',
 '12345',
 '123456',
 '1234567',
 '12345678',
 '123456789',
 '1234567890',
 '123qwe',
 '1q2w3e4r',
 '1qaz2wsx',
 '555555',
 '654321',
 '666666',
 '696969',
 '7777777',
 '888888',
 'Football',
 'aa123456',
 'abc123',
 'access',
 'admin',
 'adobe123',
 'ashley',
 'azerty',
 'bailey',
 'baseball',
 'batman',
 'charlie',
 'donald',
 'dragon',
 'flower',
 'football',
 'freedom',
 'hello',
 'hottie',
 'iloveyou',
 'jesus',
 'letmein',
 'login',
 'lovely',
 'loveme',
 'master',
 'michael',
 'monkey',
 'mustang',
 'ninja',
 'passw0rd',
 'password',
 'password1',
 'photoshop',
 'princess',
 'qazwsx',
 'qwerty',
 'qwerty123',
 'qwertyuiop',
 'shadow',
 'solo',
 'starwars',
 'sunshine',
 'superman',
 'trustno1',
 'welcome',
 'whatever',
 'zaq1zaq1'}

import requests

for password in passwords:
    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": password})
    cookie_value = response1.cookies.get("auth_cookie")
    cookies = {"auth_cookie": cookie_value}
    # print(cookies)

    response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)
    # print(response2.text)
    if response2.text == "You are authorized":
        print("Пароль найден! Это", password)

