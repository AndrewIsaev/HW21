from shop import Shop
from store import Store


def create_store():
    items = {
        "печеньки": 6,
        "собачки": 6,
        "коробки": 6
    }
    return Store(items)


def create_shop():
    items = {
        "собачки": 1,
        "коробки": 18
    }
    return Shop(items)
