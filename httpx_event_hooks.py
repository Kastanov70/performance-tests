from datetime import datetime

from httpx import Client, Request, Response

def log_request(request:Request):
    request.extensions["start_time"] = datetime.now()
    print(f"Request: {request.method}")

def log_response(response: Response):
    duration = datetime.now()-response.request.extensions["start_time"]
    print(f"Response: {response.status_code}")
    print(duration)

client = Client(base_url="http://localhost:8003", event_hooks={"request":[log_request], "response": [log_response]})

response = client.get("/api/v1/users/303c3019-a468-47bf-b06d-58dbb42babbc")

print(response)
print(response.request.extensions)
