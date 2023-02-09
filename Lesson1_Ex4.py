import requests

# payload = {"name": "User1"}
# response = requests.get("http://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)

# response = requests.get("https://playground.learnqa.ru/api/get_text")
# print(response.text)


response = requests.get("https://playground.learnqa.ru/api/hello")
print(response.text)