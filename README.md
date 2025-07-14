### YDB и SQLAlchemy

Примеры подключения к базе данных YDB в serverless-режиме
и выполнения запросов с использованием синхронной и асинхронной SQLAlchemy.

---
#### Подключение из функции

В папкaх **cloud_functions_** примеры подключения из облачной функции.
Для аутентификации в БД используются метаданные сервисного аккаунта,
от имени которого запущена функция.

---
#### Подключение с хоста

В папках **host_** примеры подключения,
в которых для аутентификации в БД используется авторизованный ключ сервисного аккаунта.

Получение авторизованного ключа описано в документации: https://yandex.cloud/ru/docs/iam/operations/authentication/manage-authorized-keys

Для хранения ключа используется json-файл.

---
#### Минимально необходимые роли для сервисного аккаунта:

* _functions.functionInvoker_
* _ydb.viewer_ 

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
