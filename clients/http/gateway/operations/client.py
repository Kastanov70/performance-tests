# client.py
from typing import TypedDict, Literal

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


OperationStatus = Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]

OperationType = Literal["FEE", "TOP_UP", "PURCHASE", "CASHBACK", "TRANSFER", "BILL_PAYMENT", "CASH_WITHDRAWAL"]


class OperationDict(TypedDict):
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения операций по номеру счета пользователя.
    """

    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения общей сводки по операциям по номеру счета пользователя.
    """

    accountId: str


class GetOperationQueryDict(TypedDict):
    """
    Структура данных для получения операций по номеру счета пользователя.
    """

    operation_id: str


class GetOperationQueryReceiptDict(TypedDict):
    """
    Структура данных для получения операций по номеру счета пользователя.
    """

    operation_id: str


class GetOperationsSummaryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета по номеру счета.
    """

    accountId: str


class MakeFeeOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class MakeTopUpOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class MakeCashbackOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class MakeTransferOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class MakePurchaseOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str
    category: str


class MakeBillPaymentOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class MakeCashWithdrawalOperationRequestDict(TypedDict):
    status: OperationStatus
    amount: float
    cardId: str
    accountId: str


class GetOperationsResponseDict(TypedDict):
    operations: list[OperationDict]


class GetOperationResponseDict(TypedDict):
    operation: OperationDict


class GetOperationReceiptResponseDict(TypedDict):
    receipt: OperationReceiptDict


class GetOperationsSummaryResponseDict(TypedDict):
    summary: OperationsSummaryDict


class MakeFeeOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    operation: OperationDict


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def  get_operation_api(self, operation_id: str) -> Response:
        # – GET /api/v1/operations/{operation_id}. Получение информации об операции по operation_id.
        """
        Получение информации об операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        # – GET /api/v1/operations/operation-receipt/{operation_id}. Получение чека по операции по operation_id.
        """
        Получение чека по операции по operation_id.

        :param operation_id: Идентификатор операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        # – GET /api/v1/operations. Получение списка операций для определенного счета.
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("//api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryDict) -> Response:
        # – GET /api/v1/operations/operations-summary. Получение статистики по операциям для определенного счета.
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary")

    def make_fee_operation_api(self, request: MakeFeeOperationRequestDict) -> Response:
        # – POST /api/v1/operations/make-fee-operation. Создание операции комиссии.
        """
        Создание операции комиссии.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request)

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequestDict
    ) -> Response:
        # – POST /api/v1/operations/make-top-up-operation. Создание операции пополнения.
        """
        Создание операции пополнения.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request)

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequestDict
    ) -> Response:
        # – POST /api/v1/operations/make-cashback-operation. Создание операции кэшбэка.
        """
        Создание операции кэшбэка.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request)

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequestDict
    ) -> Response:
        # – POST /api/v1/operations/make-transfer-operation. Создание операции перевода.
        """
        Создание операции перевода.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request)

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequestDict
    ) -> Response:
        # – POST /api/v1/operations/make-purchase-operation. Создание операции покупки.
        """
        Создание операции покупки.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request)

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequestDict
    ) -> Response:
        # – POST /api/v1/operations/make-bill-payment-operation. Создание операции оплаты по счету.
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request)

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestDict
    ) -> Response:
        # – POST /api/v1/operations/make-cash-withdrawal-operation. Создание операции снятия наличных денег.
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation", json=request
        )
    
    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        query = GetOperationQueryDict(operation_id=operation_id)
        response = self.get_operation_api(query)
        return response.json()
    
    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        query = GetOperationQueryReceiptDict(operation_id=operation_id)
        response = self.get_operation_receipt_api(query)
        return response.json()
    
    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()
    
    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()
    
    def make_fee_operation(self, cardId: str, accountId: str) -> MakeFeeOperationResponseDict:
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_fee_operation_api(request)
        return response.json()
    
    def make_top_up_operation(self, cardId: str, accountId: str) -> MakeTopUpOperationResponseDict:
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_top_up_operation_api(request)
        return response.json()
    
    def make_cashback_operation(self, cardId: str, accountId: str) -> MakeCashbackOperationResponseDict:
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_cashback_operation_api(request)
        return response.json()
    
    def make_transfer_operation(self, cardId: str, accountId: str) -> MakeTransferOperationResponseDict:
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_transfer_operation_api(request)
        return response.json()
    
    def make_purchase_operation(self, cardId: str, accountId: str) -> MakePurchaseOperationResponseDict:
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId,
            category="Car"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()
    
    def make_bill_payment_operation(self, cardId: str, accountId: str) -> MakeBillPaymentOperationResponseDict:
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()
    
    def make_cash_withdrawal_operation(self, cardId: str, accountId: str) -> MakeCashWithdrawalOperationResponseDict:
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


# Добавляем builder для DocumentsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
