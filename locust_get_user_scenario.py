from locust import HttpUser, task, between

from tools.fakers import fake

class GetUserScenarioUser(HttpUser):
    wait_time = between(1, 3)
    user_data:dict

    @task
    def get_data(self):
        self.client.get(f"/api/v1/users/{self.user_data["user"]["id"]}", name="/api/v1/users/{user_id}")
    
    def on_start(self) -> None:
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)
        print(response.text)
        self.user_data = response.json()