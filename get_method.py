import requests
url = "https://jsonplaceholder.typicode.com/posts/10"

responce = requests.get(url)
print(responce.status_code)
print(responce.json())
#print(responce.headers)
responce.close()