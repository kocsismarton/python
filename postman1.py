import requests

user="postman"
passwd="password"
valasz = requests.get("https://postman-echo.com/basic-auth", auth=(user,passwd))
print(valasz.json())
print(valasz.headers)
print(valasz.status_code)

