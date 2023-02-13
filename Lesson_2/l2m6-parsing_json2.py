from json.decoder import JSONDecodeError
import requests

# response = requests.get("https://playground.learnqa.ru/api/hello", params={"name": "User"})
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])

try:
    response = requests.get("https://playground.learnqa.ru/api/get_text")
    print(response.text)
    parsed_response_text = response.json()
except JSONDecodeError:
    print("JSON is not a JSON format")
