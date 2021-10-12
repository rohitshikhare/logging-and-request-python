import requests
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.status_code) # 200 The requested action was successful.
print(response.json())

response.close()