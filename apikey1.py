import requests

headers = {
	"x-api-key": "DEMO_API_KEY" 
}
valasz = requests.get("https://api.thecatapi.com/v1/breeds", headers=headers)
if valasz.status_code == 200:
	print(valasz.json())
else:
	print(valasz.status_code)

