from abc import ABC, abstractmethod


class Storage(ABC):
    def __init__(self, items: dict[str, int], capacity: int):
        self._items = items
        self._capacity = capacity

    @property
    @abstractmethod
    def items(self):
        return self._items

    @property
    @abstractmethod
    def capacity(self):
        return self._capacity

    @abstractmethod
    def add(self, title: str, quantity: int) -> None:
        pass

    @abstractmethod
    def remove(self, title: str, quantity: int) -> None:
        pass

    @abstractmethod
    def get_free_space(self) -> int:
        pass

    @abstractmethod
    def get_items(self) -> str:
        pass

    @abstractmethod
    def get_unique_items_count(self) -> int:
        pass
