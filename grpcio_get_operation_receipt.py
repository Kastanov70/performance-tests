# Импорт основных модулей gRPC
import grpc

# Импорт сгенерированных protobuf-сообщений для сервиса пользователей
# (структуры данных для создания пользователя)
from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
# Импорт сгенерированных gRPC Stub-классов (клиентские заглушки)
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub
# Импорт утилиты для генерации тестовых данных
from tools.fakers import fake

# Импорты для дебетового счета
from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (
    OpenDebitCardAccountRequest,
    OpenDebitCardAccountResponse
)

# Импорты для выполнения операции пополнения счета
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest,
    MakeTopUpOperationResponse
)
from contracts.services.operations.operation_pb2 import OperationStatus

# Импорты для получения чека
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest,
    GetOperationReceiptResponse
)

# Создание insecure-канала подключения к gRPC-серверу
# Используется localhost:9003 (только для локальной разработки)
channel = grpc.insecure_channel("localhost:9003")

# Создание клиента (stub) для сервиса пользователей
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
operations_gateway_service = OperationsGatewayServiceStub(channel)

# Создаем нового пользователя
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

# Открываем пользователю дебетовый счёт
open_debit_card_request = OpenDebitCardAccountRequest(user_id=create_user_response.user.id)
open_debit_card_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(open_debit_card_request)
print("Open debit card account response:", open_debit_card_response)

# Выполняем операцию пополнения счёта
make_top_up_operation_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=open_debit_card_response.account.cards[0].id,
    account_id=open_debit_card_response.account.id
)
make_top_up_operation_response:MakeTopUpOperationResponse = operations_gateway_service.MakePurchaseOperation(make_top_up_operation_request)
print("Make top up operation response:", make_top_up_operation_response)

# Получаем чек по операции и выведем его
get_operation_receipt_request = GetOperationReceiptRequest(operation_id=make_top_up_operation_response.operation.id)
get_operation_receipt_response: GetOperationReceiptResponse = operations_gateway_service.GetOperationReceipt(get_operation_receipt_request)
print("Get operation receipt response:", get_operation_receipt_response)