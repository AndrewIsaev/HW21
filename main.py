from exeptions import BaseError
from request import Request
from utils import create_store, create_shop

if __name__ == '__main__':
    store = create_store()
    shop = create_shop()

    print("Приглашение")
    while True:
        user_input = input()
        user_request = Request([store, shop], user_input)
        try:
            user_request.execute()
        except BaseError as error:
            print(error.message)
            continue

        print(f"На складе хранится:")
        print(store.get_items())
        print(f"\nВ магазине хранится:")
        print(shop.get_items())
