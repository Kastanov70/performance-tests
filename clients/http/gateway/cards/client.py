# client.py
from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient


class CreateCardsRequestDict(TypedDict):
    """
    Структура данных для создания новой карты.
    """
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/cards сервиса http-gateway.
    """

    def issue_virtual_card_api(self, request: CreateCardsRequestDict) -> Response:
        """
        Создать виртуальную карту для пользователя userId на счете accountId.

        :param request: Словарь с данными пользователя и счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post(f"/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: CreateCardsRequestDict) -> Response:
        """
        Создать физическую карту для пользователя userId на счете accountId.

        :param request: Словарь с данными пользователя и счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)
