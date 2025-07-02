from http.client import responses

import requests

# URL data, headers en params gedefineerd
url = 'https://jsonplaceholder.typicode.com/posts'
data = {'title': 'een nieuwe post', 'body': 'Dit is de inhoud van mijn nieuwe post.'}
headers = {'Content type': 'application/json'}
params = {'key': 'value'} # voorbeeld van een parameter

# Verstuur het POST-verzoek met data, headers en params
response = requests.post(url, json=data, headers=headers, params=params)

# Controleer de respons en print resultaat
if response.ok:
    print(f"Succesvol aangemaakt: {response.json()} ")
else:
    print(f"Er is iets misgegaan. Status code: {response.status_code}")
