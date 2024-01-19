import requests

api_endpoint = "http://localhost:3000/api/v1/analysis/"
image_uri = "https://github.com/Azure-Samples/cognitive-services-python-sdk-samples/raw/master/samples/vision/images/make_things_happen.jpg"

json_data = {"uri": image_uri}

response = requests.get(api_endpoint, json=json_data)

print(response.json())
