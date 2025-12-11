import requests
import json

h = {
	"Authorization": "Bearer {token}",
	"Accept": "application/json"
}
valasz = requests.get("https://reqbin.com/echo/get/json", headers=h)
if valasz.status_code == 200:
	print(valasz.json())
else:
	print(valasz.status_code)

