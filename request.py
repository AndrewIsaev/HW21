from exeptions import BaseError
from storage import Storage


class Request:
    def __init__(self, storage_list: list[Storage], request: str):
        self.storage_list = storage_list
        self.where = request.split()[4]
        self.to = request.split()[-1]
        self.amount = int(request.split()[1])
        self.product = request.split()[2]

    def execute(self) -> None:
        if self.where == "склад" and self.to == "магазин":
            self.storage_list[0].remove(self.product, self.amount)

            print(f"Курьер забирает {self.amount} {self.product} из {self.where}а")
            print(f"Курьер везет {self.amount} {self.product} из {self.where}а в {self.to}")

            try:
                self.storage_list[1].add(self.product, self.amount)
                print(f"Курьер доставил {self.amount} {self.product} в {self.to}")
            except BaseError as e:
                self.return_item(storage=0)
                print(e.message)

        elif self.where == "магазин" and self.to == "склад":
            self.storage_list[1].remove(self.product, self.amount)

            print(f"Курьер забирает {self.amount} {self.product} из {self.where}а")
            print(f"Курьер везет {self.amount} {self.product} из {self.where}а в {self.to}")

            try:
                self.storage_list[0].add(self.product, self.amount)
                print(f"Курьер доставил {self.amount} {self.product} в {self.to}")
            except BaseError as e:
                self.return_item(storage=1)
                print(e.message)

    def return_item(self, storage: int) -> None:
        self.storage_list[storage].add(self.product, self.amount)
