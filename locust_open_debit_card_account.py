from locust import HttpUser, task, between

from tools.fakers import fake

class OpenDebitCardAccountScenarioUser(HttpUser):
    wait_time = between(1, 3)
    user_id:str

    @task
    def open_debit_card_account(self):
        # Задачу @task, которая:
        # отправляет запрос POST /api/v1/accounts/open-debit-card-account;
        # передаёт ранее полученный user_id в теле запроса.
        request = {
            "userId": f"{self.user_id}"
        }
        self.client.post("/api/v1/accounts/open-debit-card-account", json=request)
    
    def on_start(self) -> None:
        # Create User
        request = {
            "email": fake.email(),
            "lastName": fake.last_name(),
            "firstName": fake.first_name(),
            "middleName": fake.middle_name(),
            "phoneNumber": fake.phone_number()
        }
        response = self.client.post("/api/v1/users", json=request)
        self.user_id = response.json()["user"]["id"]