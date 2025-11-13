import requests
import json

h={'Content-Type': 'application/json'}
d={   
      "id": 5,
      "nev": "Gatya",
      "ar": 1500,
      "beszerzesiHely": "Budapest",
      "beszerzesiIdo": "2025-08-01",
      "meretek": ["L", "XL"],
      "szin": "zöld",
      "anyag": "farmer",
      "darabszam": 5
    }

valasz = requests.post("http://localhost:3000/ruhakeszlet/", headers=h, data=json.dumps(d))
print(valasz.status_code)
#print(valasz.headers)

