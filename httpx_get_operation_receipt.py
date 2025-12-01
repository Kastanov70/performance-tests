# httpx_get_operation_receipt.py
import time

import httpx  # Импортируем библиотеку HTTPX


# 1. Создать пользователя. Выполнить POST-запрос на эндпоинт: POST /api/v1/users → Получить userId из ответа.
# Данные для создания пользователя
create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string",
    "phoneNumber": "string"
}

# Выполняем запрос на создание пользователя
create_user_response = httpx.post("http://localhost:8003/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
user_id = create_user_response_data['user']['id']

# 2. Создать кредитный счёт для пользователя. 
# Выполнить POST-запрос на эндпоинт: POST /api/v1/accounts/open-credit-card-account
open_credit_card_account_payload = {
  "userId": f"{user_id}"
}

open_credit_card_account_response = httpx.post(
	"http://localhost:8003/api/v1/accounts/open-credit-card-account",
	json=open_credit_card_account_payload
)
open_credit_card_account_data = open_credit_card_account_response.json()

# Получить accountId и cardId из ответа (кредитный счёт создаётся с картой).
account_id = open_credit_card_account_data["account"]["id"]
card_id = open_credit_card_account_data["account"]["cards"][0]["id"]

# 3. Совершить операцию покупки (purchase). Выполнить POST-запрос: POST /api/v1/operations/make-purchase-operation.
purchase_operation_payload = {
    "status": "IN_PROGRESS",
    "amount": 77.99,
    "cardId": card_id,
    "accountId": account_id,
    "category": "taxi"
}
purchase_operation_response = httpx.post(
	"http://localhost:8003/api/v1/operations/make-purchase-operation",
	json=purchase_operation_payload
)
purchase_operation_data = purchase_operation_response.json()

# Получить operationId из ответа.
operation_id = purchase_operation_data["operation"]["id"]

# 4. Получить чек по операции. Выполнить GET-запрос: GET /api/v1/operations/operation-receipt/{operation_id}
operation_receipt_response = httpx.get(
	f"http://localhost:8003/api/v1/operations/operation-receipt/{operation_id}"
)
operation_receipt_data = operation_receipt_response.json()

# 5. Распечатать JSON-ответ с данными чека в консоль.
print(f"{operation_receipt_data}")