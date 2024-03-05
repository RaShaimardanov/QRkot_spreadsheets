# QRKot Spreadseets - приложение для Благотворительного фонда

## Возможности проекта QRKot Spreadseets

- Создание благотворительных проектов
- Внесение пожертвований пользователями
- Автоматическое поступление пожертвований в открытые проекты
- Регистрация пользователей на основе FastAPI Users
- Возможность выгрузки отчёта о закрытых проектах в Google Sheets

## Технологии

[![Python](https://img.shields.io/badge/Python-000?style=for-the-badge)](https://www.python.org/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-000?style=for-the-badge)](https://www.sqlalchemy.org/)
[![Pydantic](https://img.shields.io/badge/Pydantic-000?style=for-the-badge)](https://docs.pydantic.dev/latest/)
[![FastAPI](https://img.shields.io/badge/FastAPI-000?style=for-the-badge)](https://fastapi.tiangolo.com/)
[![GoogleAPI](https://img.shields.io/badge/google-000?style=for-the-badge)](https://pypi.org/project/aiogoogle/)

## Установка и запуск проекта

- В корневой папке создайте файл *.env* и добавьте в него свои данные (при необходимости):

```
APP_TITLE=         # Название приложения
APP_DESCRIPTION=   # Описание приложения
DATABASE_URL=      # Путь подключения к БД
TYPE=service_account
PROJECT_ID=atomic-climate-<идентификатор>
PRIVATE_KEY_ID=<id приватного ключа>
PRIVATE_KEY="-----BEGIN PRIVATE KEY-----<приватный ключ>-----END PRIVATE KEY-----\n"
CLIENT_EMAIL=<email сервисного аккаунта>
CLIENT_ID=<id сервисного аккаунта>
AUTH_URI=https://accounts.google.com/o/oauth2/auth
TOKEN_URI=https://oauth2.googleapis.com/token
AUTH_PROVIDER_X509_CERT_URL=https://www.googleapis.com/oauth2/v1/certs
CLIENT_X509_CERT_URL=<ссылка>
EMAIL=<email пользователя>
```
- Установите зависимости
```shell
pip install -r requirements.txt
```
- Создайте миграции

```shell
alembic revision --autogenerate -m "First migration" 
```

- Установите миграции

```shell
alembic upgrade head
```

- Запустите проект

```shell
uvicorn main:app  --reload
```

## Примеры некоторых запросов API

|Метод   |URL                             |Описание                                             |
|:------:|:-------------------------------|:----------------------------------------------------|
| GET    | /charity_project/              | Получить список всех проектов                       |
| POST   | /charity_project/              | Добавление нового проекта                           |
| PATCH  | /charity_project/{project_id}  | Обновление данных проекта                           |
| DELETE | /charity_project/{project_id}  | Удаление проекта                                    |
| GET    | /donation/                     | Получение всех пожертвований                        |
| POST   | /donation/                     | Добавление нового пожертвования                     |
| GET    | /donation/my                   | Получить список пожертвований пользователя          |
| POST   | /google/                       | Выгрузка отчета о закрытых проектах в Google Sheets |

## Документация проекта

После запуска проекта откройте одну из ссылкок в браузере:

```shell
http://127.0.0.1:8000/docs
```

```shell
http://127.0.0.1:8000/redoc
```

## Автор проекта:

- [Расим Шаймарданов](https://github.com/RaShaimardanov/)
