class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughtSpace(BaseError):
    message = "Недостаточно места"


class NotEnoughtAmount(BaseError):
    message = "Недостаточно товара"


class UnknownTitle(BaseError):
    message = "Неизвестный товар"
