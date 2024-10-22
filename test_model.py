import requests

url = "http://127.0.0.1:8000/predict/"
data = {
    "size": 120.0,
    "nb_bedrooms": 3,
    "garden": True
}

response = requests.post(url, json=data)
if response.status_code == 200:
    print("Prediction:", response.json())
else:
    print(f"Error: {response.status_code}")