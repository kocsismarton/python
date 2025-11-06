import requests

id=input("Adj meg egy szamot: ")
valasz = requests.delete("http://localhost:3000/ruhakeszlet/" + id)
print(valasz.status_code)
#print(valasz.headers)

