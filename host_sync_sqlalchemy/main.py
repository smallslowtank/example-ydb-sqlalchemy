from queries import ORM


def main():
    query = ORM.list_users()
    print("Users:", query)


main()