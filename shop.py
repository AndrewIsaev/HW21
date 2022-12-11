from store import Store


class Shop(Store):
    def __init__(self, items: dict, capacity: int = 20):
        super().__init__(items, capacity)

    def add(self, title: str, quantity: int):
        if self.get_unique_items_count() > 5:
            print("Магазин заполнен")
        else:
            super().add(title, quantity)
