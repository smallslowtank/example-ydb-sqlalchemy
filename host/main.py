import logging
from queries import ORM


def main():
    logging.basicConfig(level=logging.INFO)
    logging.getLogger("_sqlalchemy.engine").setLevel(logging.INFO)

    orm = ORM.list_items()
    print("orm:", orm)


if __name__ == "__main__":
    main()
