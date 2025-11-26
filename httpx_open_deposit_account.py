# httpx_open_deposit_account.py
import time

import httpx


with httpx.Client() as client:
    # Создайте нового пользователя.
    create_user_payload = {
        "email": f"user.{time.time()}@example.com",
        "lastName": "string",
        "firstName": "string",
        "middleName": "string",
        "phoneNumber": "string",
    }
    create_user_response = client.post(
        "http://localhost:8003/api/v1/users", json=create_user_payload
    )
    create_user_response_data = create_user_response.json()

    # Откройте депозитный счёт.
    create_deposit_account_payload = {
        "userId": f"{create_user_response_data['user']['id']}"
    }
    create_deposit_account_response = client.post(
        "http://localhost:8003/api/v1/accounts/open-deposit-account",
        json=create_deposit_account_payload,
    )
    create_deposit_account_data = create_deposit_account_response.json()

    # Выведите результат в консоль.
    print("Create Account response:", create_deposit_account_data)
    print("Status Code:", create_deposit_account_response.status_code)
