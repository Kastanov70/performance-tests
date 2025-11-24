import httpx


# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.status_code)
# print(response.json())


# data = {
# 	"title" : "New task",
# 	"completed" : False,
# 	"userId" : 1
# }

# response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)
# print(response.status_code)
# print(response.json())

# params = {"userId": 1}

# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
# print(response.status_code)
# print(response.json())
# print(response.request.url, response.request.url.query)

with httpx.Client() as client:
    response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response1.json())  # Данные первой задачи
print(response2.json())  # Данные второй задачи


