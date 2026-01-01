from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationsQuerySchema,
    GetOperationsSummarySchema,
    MakeFeeOperationRequestSchema,
    MakeTopUpOperationRequestSchema,
    MakeCashbackOperationRequestSchema,
    MakeTransferOperationRequestSchema,
    MakePurchaseOperationRequestSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeCashWithdrawalOperationRequestSchema,
    GetOperationResponseSchema,
    GetOperationQuerySchema,
    GetOperationReceiptResponseSchema,
    GetOperationQueryReceiptSchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryResponseSchema,
    GetOperationsSummaryQuerySchema,
    MakeFeeOperationResponseSchema,
    MakeTopUpOperationResponseSchema,
    MakeCashbackOperationResponseSchema,
    MakeTransferOperationResponseSchema,
    MakePurchaseOperationResponseSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationResponseSchema
)


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        # – GET /api/v1/operations. Получение списка операций для определенного счета.
        """
        Получение списка операций для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("//api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummarySchema) -> Response:
        # – GET /api/v1/operations/operations-summary. Получение статистики по операциям для определенного счета.
        """
        Получение статистики по операциям для определенного счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, request: MakeFeeOperationRequestSchema) -> Response:
        # – POST /api/v1/operations/make-fee-operation. Создание операции комиссии.
        """
        Создание операции комиссии.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-fee-operation", json=request.model_dump(by_alias=True))

    def make_top_up_operation_api(
        self, request: MakeTopUpOperationRequestSchema
    ) -> Response:
        # – POST /api/v1/operations/make-top-up-operation. Создание операции пополнения.
        """
        Создание операции пополнения.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=request.model_dump(by_alias=True))

    def make_cashback_operation_api(
        self, request: MakeCashbackOperationRequestSchema
    ) -> Response:
        # – POST /api/v1/operations/make-cashback-operation. Создание операции кэшбэка.
        """
        Создание операции кэшбэка.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=request.model_dump(by_alias=True))

    def make_transfer_operation_api(
        self, request: MakeTransferOperationRequestSchema
    ) -> Response:
        # – POST /api/v1/operations/make-transfer-operation. Создание операции перевода.
        """
        Создание операции перевода.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=request.model_dump(by_alias=True))

    def make_purchase_operation_api(
        self, request: MakePurchaseOperationRequestSchema
    ) -> Response:
        # – POST /api/v1/operations/make-purchase-operation. Создание операции покупки.
        """
        Создание операции покупки.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=request.model_dump(by_alias=True))

    def make_bill_payment_operation_api(
        self, request: MakeBillPaymentOperationRequestSchema
    ) -> Response:
        # – POST /api/v1/operations/make-bill-payment-operation. Создание операции оплаты по счету.
        """
        Создание операции оплаты по счету.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=request.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(
        self, request: MakeCashWithdrawalOperationRequestSchema
    ) -> Response:
        # – POST /api/v1/operations/make-cash-withdrawal-operation. Создание операции снятия наличных денег.
        """
        Создание операции снятия наличных денег.

        :param request: Словарь с данными пользователя и счета, суммы и статуса операции.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(
            "/api/v1/operations/make-cash-withdrawal-operation", json=request.model_dump(by_alias=True)
        )
    
    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        query = GetOperationQuerySchema(operation_id=operation_id)
        response = self.get_operation_api(query)
        return GetOperationResponseSchema.model_validate_json(response.text)
    
    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        query = GetOperationQueryReceiptSchema(operation_id=operation_id)
        response = self.get_operation_receipt_api(query)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)
    
    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        query = GetOperationsQuerySchema(accountId=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)
    
    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        query = GetOperationsSummaryQuerySchema(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)
    
    def make_fee_operation(self, cardId: str, accountId: str) -> MakeFeeOperationResponseSchema:
        request = MakeFeeOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)
    
    def make_top_up_operation(self, cardId: str, accountId: str) -> MakeTopUpOperationResponseSchema:
        request = MakeTopUpOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)
    
    def make_cashback_operation(self, cardId: str, accountId: str) -> MakeCashbackOperationResponseSchema:
        request = MakeCashbackOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)
    
    def make_transfer_operation(self, cardId: str, accountId: str) -> MakeTransferOperationResponseSchema:
        request = MakeTransferOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)
    
    def make_purchase_operation(self, cardId: str, accountId: str) -> MakePurchaseOperationResponseSchema:
        request = MakePurchaseOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId,
            category="Car"
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)
    
    def make_bill_payment_operation(self, cardId: str, accountId: str) -> MakeBillPaymentOperationResponseSchema:
        request = MakeBillPaymentOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_bill_payment_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)
    
    def make_cash_withdrawal_operation(self, cardId: str, accountId: str) -> MakeCashWithdrawalOperationResponseSchema:
        request = MakeCashWithdrawalOperationRequestSchema(
            status="COMPLETED",
            amount=55.77,
            cardId=cardId,
            accountId=accountId
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)


# Добавляем builder для DocumentsGatewayHTTPClient
def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    """
    Функция создаёт экземпляр OperationsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return OperationsGatewayHTTPClient(client=build_gateway_http_client())
