import requests

keres = input("Adj meg egy kerest: ")
try:
	valasz = requests.get("http://localhost:3000/ruhakeszlet" + keres)
except:
	print("Valami hiba!")
	exit()
if valasz.status_code == 200:
	print(valasz.json())
print(valasz.status_code)
#print(valasz.headers)

