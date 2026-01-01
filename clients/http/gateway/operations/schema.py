from pydantic import BaseModel, Field, ConfigDict
from enum import StrEnum

class OperationStatus(StrEnum):
    """
    Перечисление статусов операций.
    
    Attributes:
        FAILED: Операция завершилась с ошибкой.
        COMPLETED: Операция успешно завершена.
        IN_PROGRESS: Операция выполняется.
        UNSPECIFIED: Статус не указан.
    """
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"

class OperationType(StrEnum):
    """
    Перечисление типов операций.
    
    Attributes:
        FEE: Комиссия.
        TOP_UP: Пополнение счёта.
        PURCHASE: Покупка товара или услуги.
        CASHBACK: Кэшбэк.
        TRANSFER: Перевод средств.
        BILL_PAYMENT: Оплата счёта.
        CASH_WITHDRAWAL: Снятие наличных.
    """
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationSchema(BaseModel):
    """
    Основная схема операции (транзакции).
    
    Attributes:
        id: Уникальный идентификатор операции.
        type: Тип операции из перечисления OperationType.
        status: Статус операции из перечисления OperationStatus.
        amount: Сумма операции (отрицательная для расходов, положительная для доходов).
        card_id: Идентификатор карты, через которую проведена операция.
        category: Категория операции (например, "Супермаркеты", "Транспорт").
        created_at: Дата и время создания операции в формате строки.
        account_id: Идентификатор счёта, к которому относится операция.
    """
    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Схема данных чека по операции.
    
    Attributes:
        url: URL-адрес для доступа к электронному чеку.
        document: Документ чека в строковом формате (например, JSON или XML).
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Схема финансовой сводки по операциям за период.
    
    Attributes:
        spent_amount: Общая сумма потраченных средств.
        received_amount: Общая сумма полученных средств.
        cashback_amount: Общая сумма полученного кэшбэка.
    """
    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationsQuerySchema(BaseModel):
    """
    Схема запроса для получения списка операций по счёту.
    
    Attributes:
        account_id: Идентификатор счёта пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Схема запроса для получения сводной статистики по операциям.
    
    Attributes:
        account_id: Идентификатор счёта пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetOperationQuerySchema(BaseModel):
    """
    Схема запроса для получения детальной информации об одной операции.
    
    Attributes:
        operation_id: Уникальный идентификатор операции.
    """
    operation_id: str


class GetOperationQueryReceiptSchema(BaseModel):
    """
    Схема запроса для получения чека по конкретной операции.
    
    Attributes:
        operation_id: Уникальный идентификатор операции.
    """
    operation_id: str


class GetOperationsSummarySchema(BaseModel):
    """
    Схема запроса для получения статистики по операциям.
    
    Attributes:
        account_id: Идентификатор счёта пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции комиссии.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма комиссии.
        card_id: Идентификатор карты, к которой относится операция.
        account_id: Идентификатор счёта, к которому относится операция.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTopUpOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции пополнения счёта.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма пополнения.
        card_id: Идентификатор карты, через которую выполняется пополнение.
        account_id: Идентификатор счёта, который пополняется.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashbackOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции кэшбэка.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма кэшбэка.
        card_id: Идентификатор карты, к которой начисляется кэшбэк.
        account_id: Идентификатор счёта, к которому относится операция.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeTransferOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции перевода средств.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма перевода.
        card_id: Идентификатор карты, с которой выполняется перевод.
        account_id: Идентификатор счёта, с которого выполняется перевод.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakePurchaseOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции покупки.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма покупки.
        card_id: Идентификатор карты, с которой выполняется оплата.
        account_id: Идентификатор счёта, к которому относится операция.
        category: Категория покупки (например, "Продукты", "Развлечения").
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")
    category: str


class MakeBillPaymentOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции оплаты счёта.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма оплаты.
        card_id: Идентификатор карты, с которой выполняется оплата.
        account_id: Идентификатор счёта, к которому относится операция.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeCashWithdrawalOperationRequestSchema(BaseModel):
    """
    Схема запроса для создания операции снятия наличных.
    
    Attributes:
        status: Статус создаваемой операции.
        amount: Сумма снятия наличных.
        card_id: Идентификатор карты, с которой выполняется снятие.
        account_id: Идентификатор счёта, к которому относится операция.
    """
    model_config = ConfigDict(populate_by_name=True)
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class GetOperationsResponseSchema(BaseModel):
    """
    Схема ответа на запрос получения списка операций.
    
    Attributes:
        operations: Список объектов OperationSchema.
    """
    operations: list[OperationSchema]


class GetOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос получения детальной информации об операции.
    
    Attributes:
        operation: Объект OperationSchema с детальной информацией об операции.
    """
    operation: OperationSchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Схема ответа на запрос получения чека по операции.
    
    Attributes:
        receipt: Объект OperationReceiptSchema с данными чека.
    """
    receipt: OperationReceiptSchema


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Схема ответа на запрос получения финансовой сводки.
    
    Attributes:
        summary: Объект OperationsSummarySchema со сводной статистикой.
    """
    summary: OperationsSummarySchema


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции комиссии.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции пополнения.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции кэшбэка.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции перевода.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции покупки.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции оплаты счёта.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Схема ответа на запрос создания операции снятия наличных.
    
    Attributes:
        operation: Созданный объект OperationSchema.
    """
    operation: OperationSchema
