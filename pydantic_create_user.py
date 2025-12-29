from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    """
    Схема для представления данных пользователя.

    Используется для отображения информации о пользователе при чтении данных.

    Attributes:
        id (str): Уникальный идентификатор пользователя в системе.
        email (EmailStr): Адрес электронной почты пользователя (валидируется на корректность формата).
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
        phoneNumber (str): Номер телефона пользователя в строковом формате.
    """
    id: str
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserRequestSchema(BaseModel):
    """
    Схема для валидации входящих данных при создании нового пользователя.

    Используется как модель запроса для endpoint'а POST /api/v1/users создания пользователя.
    Все поля обязательны для заполнения.

    Attributes:
        email (EmailStr): Адрес электронной почты (валидируется на корректность формата).
        lastName (str): Фамилия пользователя.
        firstName (str): Имя пользователя.
        middleName (str): Отчество пользователя.
        phoneNumber (str): Номер телефона пользователя.
    """
    email: EmailStr
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class CreateUserResponseSchema(BaseModel):
    """
    Схема для формирования ответа после успешного создания пользователя.

    Содержит объект созданного пользователя в формате UserSchema.

    Attributes:
        user (UserSchema): Объект с данными созданного пользователя.
    """
    user: UserSchema
