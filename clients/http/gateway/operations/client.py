# client.py
from typing import TypedDict, Literal

from httpx import Response, QueryParams

from clients.http.client import HTTPClient


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения операций по номеру счета пользователя.
    """

    accountId: str


class GetOperationsSummaryDict(TypedDict):
    """
    Структура данных для получения статистики по операциям для определенного счета по номеру счета.
    """

    accountId: str


OperationStatus = Literal["FAILED", "COMPLETED", "IN_PROGRESS", "UNSPECIFIED"]


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


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
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
