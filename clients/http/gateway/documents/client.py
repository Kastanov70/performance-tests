# client.py
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class DocumentDict(TypedDict):
    """
    Словарь с информацией о документе.
    
    Атрибуты:
        url: URL для доступа к документу.
        document: Содержимое или идентификатор документа.
    """
    url: str
    document: str


class GetTariffDocumentResponseDict(TypedDict):
    """
    Словарь с ответом на запрос документа тарифа.
    
    Атрибуты:
        tariff: Информация о документе тарифа.
    """
    tariff: DocumentDict


class GetContractDocumentResponseDict(TypedDict):
    """
    Словарь с ответом на запрос документа контракта.
    
    Атрибуты:
        tariff: Информация о документе контракта.
        Примечание: Название атрибута 'tariff' может быть опечаткой,
        следует уточнить у разработчиков API.
    """
    tariff: DocumentDict


class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тарифа по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракта по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")
    
    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа по счету в формате словаря.
        
        Выполняет запрос к API и преобразует ответ в типизированный словарь.
        
        Args:
            account_id: Уникальный идентификатор счета.
            
        Returns:
            GetTariffDocumentResponseDict: Словарь с данными документа тарифа.
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()
    
    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта по счету в формате словаря.
        
        Выполняет запрос к API и преобразует ответ в типизированный словарь.
        
        Args:
            account_id: Уникальный идентификатор счета.
            
        Returns:
            GetContractDocumentResponseDict: Словарь с данными документа контракта.
        """
        response = self.get_contract_document_api(account_id)
        return response.json()

# Добавляем builder для DocumentsGatewayHTTPClient
def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    """
    Функция создаёт экземпляр DocumentsGatewayHTTPClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию DocumentsGatewayHTTPClient.
    """
    return DocumentsGatewayHTTPClient(client=build_gateway_http_client())
