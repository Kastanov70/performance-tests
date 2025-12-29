from pydantic import BaseModel, EmailStr, Field


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


class CreateUserRequestSchema(BaseModel):
    """
    Схема для валидации входящих данных при создании нового пользователя.

    Используется как модель запроса для endpoint'а POST /api/v1/users создания пользователя.
    Все поля обязательны для заполнения.
    Поддерживает прием данных в формате camelCase через алиасы полей.

    Attributes:
        email (EmailStr): Адрес электронной почты (валидируется на корректность формата).
        last_name (str): Фамилия пользователя (алиас 'lastName' для camelCase).
        first_name (str): Имя пользователя (алиас 'firstName' для camelCase).
        middle_name (str): Отчество пользователя (алиас 'middleName' для camelCase).
        phone_number (str): Номер телефона пользователя (алиас 'phoneNumber' для camelCase).
    """
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """
    Схема для формирования ответа после успешного создания пользователя.

    Содержит объект созданного пользователя в формате UserSchema.
    Используется в ответах API на запрос создания пользователя.

    Attributes:
        user (UserSchema): Объект с данными созданного пользователя.
    """
    user: UserSchema
