import requests

payload = {"login": "secret_login", "password": "secret_pass"}
response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

print(response.text)
print(response.status_code)
print(dict(response.cookies))


print(response.headers)


payload = {"login": "secret_login", "password": "secret_pass"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get("auth_cookie")

cookies = {"auth_cookie": cookie_value}

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)



# payload = {"login": "secret_login", "password": "secret_pass"}
# response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", params=payload)
# print(response1.cookies.get("auth_cookie"))
#
# response2 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# cookie_value = response2.cookies.get("auth_cookie")
# print(response2.cookies.get("auth_cookie"))
