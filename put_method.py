import requests
# update i.e put

url = "https://jsonplaceholder.typicode.com/posts"
data = {"userId": 3,"id": 3,"title": "title name",
    "body": "body test"}
res = requests.get(url+"/"+str(data["userId"]))
print(res.json())
res.close()

responce = requests.put(url+"/"+str(data["userId"]),json=data)
print('after put method :',end='')
print(responce.status_code)
print(responce.json()) # 200 The requested action was successful.
responce.close()