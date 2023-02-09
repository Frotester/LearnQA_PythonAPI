import requests

payload = {"name": "User1"}
response = requests.get("http://playground.learnqa.ru/api/hello", params=payload)
print(response.text)