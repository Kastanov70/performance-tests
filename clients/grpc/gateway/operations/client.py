from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import GetOperationReceiptRequest, GetOperationReceiptResponse
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import GetOperationsSummaryRequest, GetOperationsSummaryResponse
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import MakeFeeOperationRequest, MakeFeeOperationResponse
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import MakeTopUpOperationRequest, MakeTopUpOperationResponse
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import MakeCashbackOperationRequest, MakeCashbackOperationResponse
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import MakeTransferOperationRequest, MakeTransferOperationResponse
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import MakePurchaseOperationRequest, MakePurchaseOperationResponse
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import MakeBillPaymentOperationRequest, MakeBillPaymentOperationResponse
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayService(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет высокоуровневые методы для получения и создания операций.
    Инкапсулирует низкоуровневые gRPC-вызовы для работы с операциями.
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayServiceStub.
        """
        super().__init__(channel)
        
        self.stub = OperationsGatewayServiceStub(channel)  # gRPC-стаб, сгенерированный из .proto

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        get_operation_api – OperationsGatewayService.GetOperation.
        Получение информации об операции по operation_id.
        Низкоуровневый вызов метода GetOperation через gRPC.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ от сервиса с данными операции.
        """
        return self.stub.GetOperation(request)
    
    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        get_operation_receipt_api – OperationsGatewayService.GetOperationReceipt.
        Получение чека по операции по operation_id.
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.

        :param request: gRPC-запрос с данными операции.
        :return: Ответ от сервиса с данными чека.
        """
        return self.stub.GetOperationReceipt(request)
    
    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        get_operations_api – OperationsGatewayService.GetOperations.
        Получение списка операций для определенного счета.
        Низкоуровневый вызов метода GetOperations через gRPC.

        :param request: gRPC-запрос с параметрами фильтрации операций.
        :return: Ответ от сервиса со списком операций.
        """
        return self.stub.GetOperations(request)
    
    def get_operations_summary_api(self, request:GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        get_operations_summary_api – OperationsGatewayService.GetOperationsSummary.
        Получение статистики по операциям для определенного счета.
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.

        :param request: gRPC-запрос с параметрами для статистики.
        :return: Ответ от сервиса со сводной статистикой операций.
        """
        return self.stub.GetOperationsSummary(GetOperationsSummaryRequest)
    
    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        make_fee_operation_api – OperationsGatewayService.MakeFeeOperation.
        Создание операции комиссии.
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.

        :param request: gRPC-запрос с данными для создания операции комиссии.
        :return: Ответ от сервиса с результатом создания операции.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        make_top_up_operation_api – OperationsGatewayService.MakeTopUpOperation.
        Создание операции пополнения счета.
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.

        :param request: gRPC-запрос с данными для пополнения счета.
        :return: Ответ от сервиса с результатом операции пополнения.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        make_cashback_operation_api – OperationsGatewayService.MakeCashbackOperation.
        Создание операции кэшбэка.
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.

        :param request: gRPC-запрос с данными для начисления кэшбэка.
        :return: Ответ от сервиса с результатом операции кэшбэка.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        make_transfer_operation_api – OperationsGatewayService.MakeTransferOperation.
        Создание операции перевода средств между счетами.
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.

        :param request: gRPC-запрос с данными для перевода.
        :return: Ответ от сервиса с результатом операции перевода.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        make_purchase_operation_api – OperationsGatewayService.MakePurchaseOperation.
        Создание операции покупки (списания средств).
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.

        :param request: gRPC-запрос с данными для операции покупки.
        :return: Ответ от сервиса с результатом операции покупки.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self, request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        make_bill_payment_operation_api – OperationsGatewayService.MakeBillPaymentOperation.
        Создание операции оплаты по счету.
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.

        :param request: gRPC-запрос с данными для оплаты счета.
        :return: Ответ от сервиса с результатом операции оплаты.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self, request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        make_cash_withdrawal_operation_api – OperationsGatewayService.MakeCashWithdrawalOperation.
        Создание операции снятия наличных денег.
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.

        :param request: gRPC-запрос с данными для снятия наличных.
        :return: Ответ от сервиса с результатом операции снятия.
        """
        return self.stub.MakeCashWithdrawalOperation(request)
    
    def get_operation(self, operation_id:str) -> GetOperationResponse:
        """
        Высокоуровневая обёртка над get_operation_api.
        Получение информации об операции по её идентификатору operation_id.

        :param operation_id: Уникальный идентификатор операции.
        :return: Ответ от сервиса с данными операции GetOperationResponse.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request=request)
    
    def get_operation_receipt(self, operation_id:str) -> GetOperationReceiptResponse:
        """
        Высокоуровневая обёртка над get_operation_receipt_api.
        Получение чека по операции по её идентификатору operation_id.

        :param operation_id: Уникальный идентификатор операции.
        :return: Ответ от сервиса с данными чека GetOperationReceiptResponse.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request=request)
    
    def get_operations (self, account_id:str) -> GetOperationsResponse:
        """
        Высокоуровневая обёртка над get_operations_api.
        Получение списка операций для счета с идентификатором account_id.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса со списком операций GetOperationsResponse.
        """
        request = GetOperationsRequest(account_id=account_id)
        return self.get_operations_api(request=request)
    
    def get_operations_summary(self, account_id:str) -> GetOperationsSummaryResponse:
        """
        Высокоуровневая обёртка над get_operations_summary_api.
        Получение статистики по операциям для счета с идентификатором account_id.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса со сводной статистикой операций GetOperationsSummaryResponse.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request=request)
    
    def make_fee_operation(self, card_id:str, account_id:str) -> MakeFeeOperationResponse:
        """
        Высокоуровневая обёртка над make_fee_operation_api.
        Создание операции комиссии с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом создания операции комиссии MakeFeeOperationResponse.
        """
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request=request)

    def make_top_up_operation(self, card_id:str, account_id:str) -> MakeTopUpOperationResponse:
        """
        Высокоуровневая обёртка над make_top_up_operation_api.
        Создание операции пополнения счета с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом операции пополнения MakeTopUpOperationResponse.
        """
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request=request)
    
    def make_cashback_operation(self, card_id:str, account_id:str) -> MakeCashbackOperationResponse:
        """
        Высокоуровневая обёртка над make_cashback_operation_api.
        Создание операции кэшбэка с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом операции кэшбэка MakeCashbackOperationResponse.
        """
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request=request)
    
    def make_transfer_operation(self, card_id:str, account_id:str) -> MakeTransferOperationResponse:
        """
        Высокоуровневая обёртка над make_transfer_operation_api.
        Создание операции перевода средств с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом операции перевода MakeTransferOperationResponse.
        """
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request=request)
    
    def make_purchase_operation(self, card_id:str, account_id:str) -> MakePurchaseOperationResponse:
        """
        Высокоуровневая обёртка над make_purchase_operation_api.
        Создание операции покупки с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом операции покупки MakePurchaseOperationResponse.
        """
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            category=fake.category(),
            account_id=account_id
        )
        return self.make_purchase_operation_api(request=request)
    
    def make_bill_payment_operation(self, card_id:str, account_id:str) -> MakeBillPaymentOperationResponse:
        """
        Высокоуровневая обёртка над make_bill_payment_operation_api.
        Создание операции оплаты по счету с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом операции оплаты MakeBillPaymentOperationResponse.
        """
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request=request)
    
    def make_cash_withdrawal_operation(self, card_id:str, account_id:str) -> MakeCashWithdrawalOperationResponse:
        """
        Высокоуровневая обёртка над make_cash_withdrawal_operation_api.
        Создание операции снятия наличных с автоматической генерацией тестовых данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ от сервиса с результатом операции снятия MakeCashWithdrawalOperationResponse.
        """
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request=request)

def build_users_gateway_grpc_client() -> OperationsGatewayService:
    """
    Фабричная функция для создания экземпляра OperationsGatewayService.
    Создает клиент с предварительно настроенным gRPC-каналом.

    :return: Инициализированный клиент OperationsGatewayService.
    """
    return OperationsGatewayService(channel=build_gateway_grpc_client())
