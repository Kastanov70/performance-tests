import time

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema
)


class UsersGatewayHTTPClient(HTTPClient):
    """
    HTTP-клиент для работы с API пользователей через шлюз (gateway).
    
    Обеспечивает взаимодействие с эндпоинтами /api/v1/users сервиса http-gateway.
    Предоставляет методы двух уровней:
    1. Низкоуровневые методы с суффиксом _api - возвращают сырые httpx.Response объекты
    2. Высокоуровневые методы - возвращают валидированные Pydantic-модели
    """

    def get_user_api(self, user_id: str) -> Response:
        """
        Выполняет GET-запрос для получения данных пользователя по ID.
        
        Эндпоинт: GET /api/v1/users/{user_id}
        
        Args:
            user_id: Уникальный строковый идентификатор пользователя.
            
        Returns:
            httpx.Response: Ответ сервера, содержащий статус-код, заголовки и тело ответа.
            
        Raises:
            httpx.HTTPStatusError: При получении статус-кода 4xx или 5xx от сервера.
        """
        return self.get(f"/api/v1/users/{user_id}")

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания нового пользователя.
        
        Эндпоинт: POST /api/v1/users
        
        Args:
            request: Схема CreateUserRequestSchema с данными нового пользователя.
            
        Returns:
            httpx.Response: Ответ сервера с результатом операции создания.
            
        Note:
            Данные сериализуются с использованием model_dump(by_alias=True) для 
            сохранения camelCase формата в JSON-теле запроса.
            
        Raises:
            httpx.HTTPStatusError: При ошибках валидации или конфликтах данных.
        """
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        """
        Получает данные пользователя и валидирует их в Pydantic-схему.
        
        Использует get_user_api() для выполнения запроса, затем парсит JSON-ответ
        и валидирует его с помощью GetUserResponseSchema.
        
        Args:
            user_id: Уникальный строковый идентификатор пользователя.
            
        Returns:
            GetUserResponseSchema: Валидированная схема с данными пользователя.
            
        Raises:
            pydantic.ValidationError: Если структура ответа не соответствует схеме.
            httpx.HTTPStatusError: При ошибках HTTP-запроса.
        """
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        """
        Создает тестового пользователя с автоматически сгенерированными данными.
        
        Генерирует уникальный email на основе временной метки и использует
        фиксированные тестовые значения для остальных полей. После создания
        валидирует ответ в CreateUserResponseSchema.
        
        Returns:
            CreateUserResponseSchema: Валидированная схема с данными созданного пользователя.
            
        Note:
            Предназначен в первую очередь для тестирования и демонстрации работы API.
            Для создания пользователей с произвольными данными используйте create_user_api().
            
        Raises:
            pydantic.ValidationError: Если структура ответа не соответствует схеме.
            httpx.HTTPStatusError: При ошибках HTTP-запроса.
        """
        request = CreateUserRequestSchema(
            email=f"user.{time.time()}@example.com",
            last_name="string",
            first_name="string",
            middle_name="string",
            phone_number="string"
        )
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)


def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    """
    Фабричная функция для создания предварительно настроенного клиента пользователей.
    
    Создает и возвращает экземпляр UsersGatewayHTTPClient, используя
    настроенный HTTP-клиент для шлюза (gateway).
    
    Returns:
        UsersGatewayHTTPClient: Готовый к использованию клиент для работы с API пользователей.
        
    Example:
        >>> client = build_users_gateway_http_client()
        >>> user_data = client.get_user("user_123")
        >>> new_user = client.create_user()
    """
    return UsersGatewayHTTPClient(client=build_gateway_http_client())
