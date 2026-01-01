from pydantic import BaseModel, HttpUrl, Field, ConfigDict


class DocumentSchema(BaseModel):
    """
    Схема документа с ссылкой и содержимым.
    
    Используется для представления документа в системе, содержащего URL для доступа
    и текстовое содержимое или идентификатор документа.

    Attributes:
        url (HttpUrl): Валидный URL-адрес для доступа к документу.
                       Автоматически валидируется на корректность формата URL.
        document (str): Содержимое документа в текстовом формате или его уникальный идентификатор.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentRequestSchema(BaseModel):
    """
    Схема запроса для получения документа тарифа.
    
    Содержит идентификатор счета, для которого требуется получить тарифный документ.
    Поддерживает получение данных в формате camelCase через алиас.

    Attributes:
        account_id (str): Уникальный идентификатор счета (принимает 'accountId' в camelCase).
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetContractDocumentRequestSchema(BaseModel):
    """
    Схема запроса для получения документа контракта.
    
    Содержит идентификатор счета, для которого требуется получить контрактный документ.
    Поддерживает получение данных в формате camelCase через алиас.

    Attributes:
        account_id (str): Уникальный идентификатор счета (принимает 'accountId' в camelCase).
    """
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Схема ответа с документом тарифа.
    
    Возвращается в ответ на запрос получения тарифного документа.
    Содержит информацию о документе тарифа в формате DocumentSchema.

    Attributes:
        tariff (DocumentSchema): Объект с данными тарифного документа.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Схема ответа с документом контракта.
    
    Возвращается в ответ на запрос получения контрактного документа.
    Содержит информацию о документе контракта в формате DocumentSchema.

    Attributes:
        contract (DocumentSchema): Объект с данными контрактного документа.
    """
    contract: DocumentSchema
