from locust import User, between, task

from clients.http.gateway.locust import GatewayHTTPTaskSet
from clients.http.gateway.users.schema import CreateUserResponseSchema


class GetAccountsTaskSet(GatewayHTTPTaskSet):
    """
    Нагрузочный сценарий, который:
    - Создаёт нового пользователя.
    - Открывает депозитный счёт.
    - Получает список всех счетов для текущего пользователя.

    Использует базовый GatewayHTTPTaskSet и уже созданных в нём API клиентов.
    """

    # Shared state — сохраняем результаты запросов для дальнейшего использования
    create_user_response: CreateUserResponseSchema | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        self.create_user_response = self.users_gateway_client.create_user()

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что пользователь был создан успешно.
        """
        if not self.create_user_response:
            return

        self.accounts_gateway_client.open_deposit_account(
            self.create_user_response.user.id
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем счета пользователя, если пользователь был создан успешно.
        """
        if not self.create_user_response:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.create_user_response.user.id)


class GetAccountsUser(User):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения счетов пользователя.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1,3)