from shop import Shop
from storage import Storage
from store import Store


def create_store() -> Storage:
    """
    Create store
    :return: Store()
    """
    items = {
        "печеньки": 6,
        "собачки": 6,
        "коробки": 6
    }
    return Store(items)


def create_shop() -> Storage:
    """
        Create shop
        :return: Shop()
        """
    items = {
        "собачки": 1,
        "коробки": 11
    }
    return Shop(items)


def is_stop(user_input) -> bool:
    """
    Check end of program
    :param user_input: user_input
    :return: True or False
    """
    if user_input in ["stop", "стоп"]:
        return True
    return False
