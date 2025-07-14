import os
import ydb.iam
from dotenv import load_dotenv

load_dotenv()


class Settings:
    cloud_id = os.getenv("CLOUD_ID")  # идентификатор облака, в котором находится БД
    db_id = os.getenv("DB_ID")  # идентификатор БД
    zone = "ru-central1"
    endpoint = "ydb.serverless.yandexcloud.net:2135"  # эндпоинт для serverless БД
    # yql+ydb синхронный диалект
    url = f"yql+ydb://{endpoint}//{zone}/{cloud_id}/{db_id}"
    # для авторизации в БД используются метаданные сервисного аккаунта
    # от имени которого запускается функция
    credentials = ydb.iam.MetadataUrlCredentials()
    # параметры подключения
    args = {
        "_add_declare_for_yql_stmt_vars": True,
        "connect_args": {
            "protocol": "grpcs",
            "credentials": credentials,
        },
    }


settings = Settings()
