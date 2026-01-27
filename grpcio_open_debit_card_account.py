# Импорт основных модулей gRPC
import grpc

# Импорт сгенерированных protobuf-сообщений для сервиса аккаунтов
# (структуры данных для запроса и ответа на открытие дебетовой карты)
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest, 
    OpenDebitCardAccountResponse
)
# Импорт сгенерированных protobuf-сообщений для сервиса пользователей
# (структуры данных для создания пользователя)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
# Импорт сгенерированных gRPC Stub-классов (клиентские заглушки)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
# Импорт утилиты для генерации тестовых данных
from tools.fakers import fake

# Создание insecure-канала подключения к gRPC-серверу
# Используется localhost:9003 (только для локальной разработки)
channel = grpc.insecure_channel("localhost:9003")

# Создание клиента (stub) для сервиса пользователей
users_gateway_service = UsersGatewayServiceStub(channel)

# Подготовка запроса на создание пользователя с тестовыми данными
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)

# Вызов удалённого метода CreateUser на сервере
# Передаём подготовленный запрос, получаем ответ
create_user_response:CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print("Create user response:", create_user_response)

# Создание клиента (stub) для сервиса аккаунтов
# Используем тот же канал подключения (переиспользуем соединение)
accounts_gateway_service = AccountsGatewayServiceStub(channel)

# Подготовка запроса на открытие дебетового счёта
# Используем ID пользователя из предыдущего ответа
open_debit_card_account_request = OpenDebitCardAccountRequest(user_id=create_user_response.user.id)

# Вызов удалённого метода OpenDebitCardAccount на сервере
open_debit_card_account__response:OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(
    open_debit_card_account_request
)
print("Open debit card account response:", open_debit_card_account__response)
