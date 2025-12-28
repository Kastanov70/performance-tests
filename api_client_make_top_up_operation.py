# Создать пользователя с помощью метода клиента UsersGatewayHTTPClient.create_user 
# (уже реализовано в данном уроке).
# Открыть дебетовый счет  AccountsGatewayHTTPClient.open_debit_card_account (уже реализовано в данном уроке).
# Создать операцию пополнения счета OperationsGatewayHTTPClient.make_top_up_operations 
# (реализуется в рамках данного задания).
# Для инициализации API-клиентов используйте следующие функции:
# build_users_gateway_http_client() (уже реализовано в данном уроке).
# build_accounts_gateway_http_client() (уже реализовано в данном уроке).
# build_operations_gateway_http_client() (реализуется в рамках данного задания).
# Вывод 
# Create user response: {'user': {'id': '61908602-1ac3-4e20-9554-85e01f63d71e', 'email': 'user.1749369721.6589901@example.com', 'lastName': 'string', 'firstName': 'string', 'middleName': 'string', 'phoneNumber': 'string'}}
# Open debit card account response: {'account': {'id': 'cc9c9dad-7cb7-4003-a5cc-e2dd3bca58d8', 'type': 'DEBIT_CARD', 'cards': [{'id': '5b8d5d34-3888-45ae-9455-7c70cf0521f7', 'pin': '9154', 'cvv': '212', 'type': 'VIRTUAL', 'status': 'ACTIVE', 'accountId': 'cc9c9dad-7cb7-4003-a5cc-e2dd3bca58d8', 'cardNumber': '4943854212695667704', 'cardHolder': 'string string', 'expiryDate': '2032-06-06', 'paymentSystem': 'MASTERCARD'}, {'id': '816fffdd-a774-4f88-8d76-0e695c5fcf8d', 'pin': '1757', 'cvv': '994', 'type': 'PHYSICAL', 'status': 'ACTIVE', 'accountId': 'cc9c9dad-7cb7-4003-a5cc-e2dd3bca58d8', 'cardNumber': '3500663622495780', 'cardHolder': 'string string', 'expiryDate': '2032-06-06', 'paymentSystem': 'MASTERCARD'}], 'status': 'ACTIVE', 'balance': 0.0}}
# Make top up operation response: {'operation': {'id': '4489f3cb-72f5-4ccd-b32c-6f4809b4687a', 'type': 'TOP_UP', 'status': 'COMPLETED', 'amount': 1500.11, 'cardId': '5b8d5d34-3888-45ae-9455-7c70cf0521f7', 'category': 'money_in', 'createdAt': '2025-06-08T08:02:03.517909', 'accountId': 'cc9c9dad-7cb7-4003-a5cc-e2dd3bca58d8'}}

from clients.http.gateway.accounts.client import build_accounts_gateway_http_client
from clients.http.gateway.operations.client import build_operations_gateway_http_client
from clients.http.gateway.users.client import build_users_gateway_http_client


users_gateway_client = build_users_gateway_http_client()
accounts_gateway_client = build_accounts_gateway_http_client()
operations_gateway_client = build_operations_gateway_http_client()

# Создаем пользователя
create_user_response = users_gateway_client.create_user()
print('Create user response:', create_user_response)

# Открываем дебетовый счет
open_debit_card_account_response = accounts_gateway_client.open_debit_card_account(
    user_id=create_user_response['user']['id']
)
print('Open debit card account response:', open_debit_card_account_response)

# Проводим операцию пополнения счета
top_up_operation_response = operations_gateway_client.make_top_up_operation(
    cardId=open_debit_card_account_response['account']['cards'][0]["id"],
    accountId=open_debit_card_account_response['account']['id']
)
print('Make top up operation response:', top_up_operation_response)
