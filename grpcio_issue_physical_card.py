# Импорт основных модулей gRPC
import grpc

# Импорт сгенерированных protobuf-сообщений для сервиса пользователей
# (структуры данных для создания пользователя)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
# Импорт сгенерированных gRPC Stub-классов (клиентские заглушки)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
# Импорт утилиты для генерации тестовых данных
from tools.fakers import fake
#  new ----
from contracts.services.gateway.accounts.rpc_open_credit_card_account_pb2 import (
    OpenCreditCardAccountRequest,
    OpenCreditCardAccountResponse
)
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub

from contracts.services.gateway.cards.rpc_issue_physical_card_pb2 import (
    IssuePhysicalCardRequest,
    IssuePhysicalCardResponse
)
from contracts.services.gateway.cards.cards_gateway_service_pb2_grpc import CardsGatewayServiceStub


# Создание insecure-канала подключения к gRPC-серверу
# Используется localhost:9003 (только для локальной разработки)
channel = grpc.insecure_channel("localhost:9003")

# Создание клиента (stub) для сервиса пользователей
users_gateway_service = UsersGatewayServiceStub(channel)
# new ---
accounts_gateway_service = AccountsGatewayServiceStub(channel)
cards_gateway_service = CardsGatewayServiceStub(channel)

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

# Open Credit card
open_credit_card_account_request = OpenCreditCardAccountRequest(user_id=create_user_response.user.id)
open_credit_card_account_response: OpenCreditCardAccountResponse = accounts_gateway_service.OpenCreditCardAccount(open_credit_card_account_request)
print("Open credit card account response:", open_credit_card_account_response)

# Issue physical card
issue_physical_card_request = IssuePhysicalCardRequest(
    user_id=create_user_response.user.id,
    account_id=open_credit_card_account_response.account.id
)
issue_physical_card_response:IssuePhysicalCardResponse = cards_gateway_service.IssuePhysicalCard(issue_physical_card_request)
print("Issue physical card response:", issue_physical_card_response)
