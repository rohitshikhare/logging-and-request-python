import requests

# create i.e post

url = "https://jsonplaceholder.typicode.com/posts"
file_data = {"userId": 2, "id": 101, "title": "qui est esse",
             "body": "est rerum tempore vitae sequi sint nihil"}

responce = requests.post(url, json=file_data)
print(responce.status_code)  # 201 A new resource was created.
print(responce.json())
responce.close()


