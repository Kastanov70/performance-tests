from locust import User, task, between

from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client
from clients.http.gateway.users.schema import CreateUserResponseSchema


class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayHTTPClient
    create_user_response: CreateUserResponseSchema
    accounts_gateway_client:  AccountsGatewayHTTPClient

    @task
    def open_debit_card_account(self):
        # Задачу @task, которая:
        # Открывает debit card счет для пользователя;
        # передаёт id созданного пользователя.
        self.accounts_gateway_client.open_credit_card_account(self.create_user_response.user.id)
    
    def on_start(self) -> None:
        # Create User
        self.users_gateway_client = build_users_gateway_locust_http_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

        # Создает accounts client для работы со счетами
        self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.environment)
