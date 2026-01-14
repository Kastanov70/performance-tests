from pydantic import BaseModel, EmailStr, Field, ConfigDict

from tools.fakers import fake


class UserSchema(BaseModel):
    """
    Схема для представления данных пользователя.

    Используется для отображения информации о пользователе при чтении данных.
    Поддерживает работу с данными в формате camelCase через алиасы полей.

    Attributes:
        id (str): Уникальный идентификатор пользователя в системе.
        email (EmailStr): Адрес электронной почты пользователя (валидируется на корректность формата).
        last_name (str): Фамилия пользователя (алиас 'lastName' для camelCase).
        first_name (str): Имя пользователя (алиас 'firstName' для camelCase).
        middle_name (str): Отчество пользователя (алиас 'middleName' для camelCase).
        phone_number (str): Номер телефона пользователя в строковом формате (алиас 'phoneNumber' для camelCase).
    """
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class GetUserResponseSchema(BaseModel):
    """
    Схема для формирования ответа при успешном получении пользователя в запросе GET api/v1/users/{user_id}.

    Содержит объект созданного пользователя в формате UserSchema.
    Используется в ответах API на запрос создания пользователя.

    Attributes:
        user (UserSchema): Объект с данными созданного пользователя.
    """
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """
    Схема для валидации входящих данных при создании нового пользователя.

    Используется как модель запроса для endpoint'а POST /api/v1/users создания пользователя.
    Все поля обязательны для заполнения.
    
    Особенности:
    - Поддерживает прием данных в формате camelCase через алиасы полей
    - Конфигурация populate_by_name=True позволяет использовать как snake_case, так и camelCase 
      при создании экземпляров модели
    - Поле email автоматически валидируется на корректность формата электронной почты

    Attributes:
        email (EmailStr): Адрес электронной почты (валидируется на корректность формата).
        last_name (str): Фамилия пользователя (принимает 'lastName' в camelCase).
        first_name (str): Имя пользователя (принимает 'firstName' в camelCase).
        middle_name (str): Отчество пользователя (принимает 'middleName' в camelCase).
        phone_number (str): Номер телефона пользователя (принимает 'phoneNumber' в camelCase).

    Note:
        При создании экземпляра можно использовать любой стиль именования:
        CreateUserRequestSchema(last_name="Иванов") или 
        CreateUserRequestSchema(lastName="Иванов")
    """
    
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr = Field(default_factory=fake.email)
    last_name: str = Field(alias="lastName", default_factory=fake.last_name)
    first_name: str = Field(alias="firstName", default_factory=fake.first_name)
    middle_name: str = Field(alias="middleName", default_factory=fake.middle_name)
    phone_number: str = Field(alias="phoneNumber", default_factory=fake.phone_number)


class CreateUserResponseSchema(BaseModel):
    """
    Схема для формирования ответа после успешного создания пользователя.

    Содержит объект созданного пользователя в формате UserSchema.
    Используется в ответах API на запрос создания пользователя.

    Attributes:
        user (UserSchema): Объект с данными созданного пользователя.
    """
    user: UserSchema
