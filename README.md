### YDB и SQLAlchemy

Примеры подключения к базе данных YDB в serverless-режиме и выполнения запросов с использованием SQLAlchemy.

#### Подключение из функции

В папке **cloud_function** пример подключения из облачной функции на Python.
Для аутентификации в БД используются метаданные сервисного аккаунта, от имени которого запущена функция.

#### Подключение с хоста

В папке **host** пример подключения,
в котором для аутентификации в БД используется авторизованный ключ сервисного аккаунта.

Получение авторизованного ключа описано в документации: https://yandex.cloud/ru/docs/iam/operations/authentication/manage-authorized-keys
Для хранения ключа используется json-файл.

---
#### Ссылки

Yandex Cloud Function

https://yandex.cloud/ru/docs/functions

Репозиторий YDB-SQLAlchemy

https://github.com/ydb-platform/ydb-sqlalchemy

Способы аутентификации в YDB

https://ydb.tech/docs/ru/recipes/ydb-sdk/auth


Подключение к YDB с помощью DBeaver

https://ydb.tech/docs/ru/integrations/gui/dbeaver

Работа с YDB с помощью Jupyter Notebook

https://ydb.tech/docs/ru/integrations/gui/jupyter
