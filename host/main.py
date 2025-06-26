from database import engine
from queries import run_example_core, ORM


def handler():
    core = run_example_core(engine)
    orm = ORM.list_users()
    return core, orm


core, orm = handler()
print("core:", core)
print("orm:", orm)
