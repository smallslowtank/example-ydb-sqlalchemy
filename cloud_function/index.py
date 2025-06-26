from database import engine
from queries import run_example_core, ORM
from config import settings

def handler(event, content):
    """
    Точка входа в функцию
    """
    core = run_example_core(engine)
    orm  = ORM.list_users()
    return {
        "core": core,
        "orm": orm
    }


print(settings.url)
print(settings.args)
print(type(settings.credentials))