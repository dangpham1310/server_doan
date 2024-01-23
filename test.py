import requests

a = requests.get("http://127.0.0.1:5000/SOIL_0001/SOIL 0001")
print(a.text)

