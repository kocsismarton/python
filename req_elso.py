import requests

valasz = requests.get(input("Adj meg egy URL-t: "))
print(valasz.status_code)
print(valasz.headers)
