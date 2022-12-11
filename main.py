from exeptions import BaseError
from request import Request
from utils import create_store, create_shop, is_stop

if __name__ == '__main__':
    # Create storages
    store = create_store()
    shop = create_shop()

    print("Введите строку вида: 'Доставить 3 печеньки из склад в магазин'")
    while True:
        user_input = input()
        # Check stop
        if is_stop(user_input):
            break

        user_request = Request([store, shop], user_input)
        # Check errors
        try:
            user_request.execute()
        except BaseError as error:
            print(error.message)
            continue
        # Show storages
        print(f"На складе хранится:")
        print(store.get_items())
        print(f"\nВ магазине хранится:")
        print(shop.get_items())
