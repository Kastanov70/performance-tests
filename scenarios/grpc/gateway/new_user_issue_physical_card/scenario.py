from locust import task

from clients.grpc.gateway.locust import GatewayGRPCSequentialTaskSet
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountResponse
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserResponse
from tools.locust.user import LocustBaseUser


class IssuePhysicalCardSequentialTaskSet(GatewayGRPCSequentialTaskSet):
    create_user_response: CreateUserResponse | None = None
    open_open_debit_card_account_response: OpenDebitCardAccountResponse | None = None

    @task
    def create_user(self):
        # Первый шаг — создать нового пользователя
        self.create_user_response = self.users_gateway_client.create_user()

    # Открытие дебетового счёта для этого пользователя;
    @task
    def open_debit_card_account(self):
        # Невозможно открыть счёт без созданного пользователя
        if not self.create_user_response:
            return

        # Открываем дебетовый счёт для нового пользователя
        self.open_open_debit_card_account_response = self.accounts_gateway_client.open_debit_card_account(
            user_id=self.create_user_response.user.id
        )

    # Выпуск физической карты, привязанной к этому счёту.
    @task
    def issue_physical_card(self):
        # Невозможно выпустить карту без счёта
        if not self.open_open_debit_card_account_response:
            return

        self.cards_gateway_client.issue_physical_card(
            user_id=self.create_user_response.user.id,
            account_id=self.open_open_debit_card_account_response.account.id
        )

class IssuePhysicalCardScenarioUser(LocustBaseUser):
    tasks = [IssuePhysicalCardSequentialTaskSet]