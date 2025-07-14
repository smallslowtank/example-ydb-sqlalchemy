from queries import ORM


def handler(event, content):
    """
    Точка входа в функцию
    """

    query = ORM.list_users()
    print("Users:", query)

    return {"status": "ok"}
