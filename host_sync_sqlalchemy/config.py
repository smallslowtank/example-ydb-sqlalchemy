import os
from dotenv import load_dotenv
import ydb.iam

load_dotenv()


class Settings:
    cloud_id = os.getenv("CLOUD_ID")  # идентификатор облака, в котором находится БД
    db_id = os.getenv("DB_ID")        # идентификатор БД
    zone = "ru-central1"
    endpoint = "ydb.serverless.yandexcloud.net:2135"  # эндпоинт для serverless БД
    # yql+ydb синхронный диалект
    url = f"yql+ydb://{endpoint}//{zone}/{cloud_id}/{db_id}"
    # для авторизации в БД используется авторизованный ключ для сервисного аккаунта
    # https://yandex.cloud/ru/docs/iam/operations/authentication/manage-authorized-keys
    # yc iam key create --service-account-name sa-name -o sa-key.json
    credentials = ydb.iam.ServiceAccountCredentials.from_file(key_file="sa-key.json")
    # параметры подключения
    args = {
        "_add_declare_for_yql_stmt_vars": True,
        "connect_args": {
            "protocol": "grpcs",
            "credentials": credentials,
        },
    }


settings = Settings()
