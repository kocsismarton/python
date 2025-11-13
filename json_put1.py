import requests
import json

h={'Content-Type': 'application/json'}
d={   
      "id": 4,
      "nev": "Gatya",
      "ar": 1200,
      "beszerzesiHely": "Budapest",
      "beszerzesiIdo": "2025-08-01",
      "meretek": ["L", "XL"],
      "szin": "zöld",
      "anyag": "farmer",
      "darabszam": 115
    }
try:
	valasz = requests.put("http://localhost:3000/ruhakeszlet/4", headers=h, data=json.dumps(d))
except:
	print("Benasag tortent!")
	exit()
print(valasz.status_code)
#print(valasz.headers)

