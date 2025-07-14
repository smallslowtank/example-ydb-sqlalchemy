from queries import ORM


async def handler(event, content):
    """
    Точка входа в функцию
    """

    query = await ORM.list_users()
    print("Users:", query)

    return {"status": "ok"}
