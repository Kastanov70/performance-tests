from pydantic import BaseModel, HttpUrl, Field, ConfigDict


class DocumentSchema(BaseModel):
    """
    Словарь с информацией о документе.
    
    Атрибуты:
        url: URL для доступа к документу.
        document: Содержимое или идентификатор документа.
    """
    url: HttpUrl
    document: str


class GetTariffDocumentRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetContractDocumentRequestSchema(BaseModel):
    model_config = ConfigDict(populate_by_name=True)
    account_id: str = Field(alias="accountId")


class GetTariffDocumentResponseSchema(BaseModel):
    """
    Словарь с ответом на запрос документа тарифа.
    
    Атрибуты:
        tariff: Информация о документе тарифа.
    """
    tariff: DocumentSchema


class GetContractDocumentResponseSchema(BaseModel):
    """
    Словарь с ответом на запрос документа контракта.
    
    Атрибуты:
        tariff: Информация о документе контракта.
        Примечание: Название атрибута 'tariff' может быть опечаткой,
        следует уточнить у разработчиков API.
    """
    contract: DocumentSchema

