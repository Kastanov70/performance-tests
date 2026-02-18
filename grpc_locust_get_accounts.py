from locust import User, between, task

from clients.grpc.gateway.locust import GatewayGRPCTaskSet


class GetAccountsTaskSet(GatewayGRPCTaskSet):
    """
    Нагрузочный сценарий, который:
    - Создаёт нового пользователя.
    - Открывает депозитный счёт.
    - Получает список всех счетов для текущего пользователя.

    Использует базовый GatewayGRPCTaskSet и уже созданных в нём API клиентов.
    """

    # Shared state — сохраняем результаты запросов для дальнейшего использования
    user_id: str | None = None

    @task(2)
    def create_user(self):
        """
        Создаём нового пользователя и сохраняем результат для последующих шагов.
        """
        create_user_response = self.users_gateway_client.create_user()
        self.user_id = create_user_response.user.id

    @task(2)
    def open_deposit_account(self):
        """
        Открываем депозитный счёт для созданного пользователя.
        Проверяем, что пользователь был создан успешно.
        """
        if not self.user_id:
            return

        self.accounts_gateway_client.open_deposit_account(
            self.user_id
        )

    @task(6)
    def get_accounts(self):
        """
        Получаем счета пользователя, если пользователь был создан успешно.
        """
        if not self.user_id:
            return

        self.accounts_gateway_client.get_accounts(user_id=self.user_id)


class GetAccountsUser(User):
    """
    Пользователь Locust, исполняющий последовательный сценарий получения счетов пользователя.
    """
    host = "localhost"
    tasks = [GetAccountsTaskSet]
    wait_time = between(1,3)