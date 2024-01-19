import requests

api_endpoint = "http://localhost:3000/api/v1/analysis/"
image_uri = "/Users/bohanliu/Documents/17645/mlip-api-lab/test-image.jpeg"

json_data = {"uri": image_uri}

response = requests.get(api_endpoint, json=json_data)

print(response.json())
