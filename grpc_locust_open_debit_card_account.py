from locust import User, task, between

from clients.grpc.gateway.accounts.client import AccountsGatewayGRPCClient, build_accounts_gateway_locust_grpc_client
from clients.grpc.gateway.users.client import UsersGatewayGRPCClient, build_users_gateway_locust_grpc_client
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse

class OpenDebitCardAccountScenarioUser(User):
    host = "localhost"
    wait_time = between(1, 3)
    users_gateway_client: UsersGatewayGRPCClient
    create_user_response: CreateUserResponse
    accounts_gateway_client: AccountsGatewayGRPCClient

    @task
    def open_debit_card_account(self):
        # Задачу @task, которая:
        # Открывает debit card счет для пользователя;
        # передаёт id созданного пользователя.
        self.accounts_gateway_client.open_credit_card_account(self.create_user_response.user.id)

    def on_start(self) -> None:
        # Create User
        self.users_gateway_client = build_users_gateway_locust_grpc_client(self.environment)
        self.create_user_response = self.users_gateway_client.create_user()

        # Создает accounts client для работы со счетами
        self.accounts_gateway_client = build_accounts_gateway_locust_grpc_client(self.environment)
