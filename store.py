from exeptions import NotEnoughSpace, NotEnoughAmount, UnknownTitle
from storage import Storage


class Store(Storage):
    def __init__(self, items: dict, capacity: int = 100):
        super().__init__(items, capacity)

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title: str, quantity: int) -> None:
        if self.get_free_space() >= quantity:
            if self._is_in_storage(title):
                self.items[title] += quantity
            else:
                self.items[title] = quantity
        else:
            raise NotEnoughSpace

    def remove(self, title: str, quantity: int) -> None:
        if self._is_in_storage(title):
            if quantity > self.items[title]:
                raise NotEnoughAmount
            else:
                print("Нужное количество есть на складе")
                self.items[title] -= quantity
        else:
            raise UnknownTitle

        if self.items[title] == 0:
            self.items.pop(title)

    def get_free_space(self) -> int:
        free_space = self.capacity - sum(self.items.values())
        if free_space < 0:
            return 0
        return free_space

    def get_items(self) -> str:
        items_list = []
        for item in self.items:
            items_list.append(f"{self.items[item]} {item}")
        return "\n".join(items_list)

    def get_unique_items_count(self) -> int:
        return len(set(self.items.keys()))

    def _is_in_storage(self, title: str) -> bool:
        if title in self.items:
            return True
        return False
