import requests
# sirve para hacer peticiones a internet
request = requests.get("https://www.google.es")

print(request.text[:50])
