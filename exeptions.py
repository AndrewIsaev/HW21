class BaseError(Exception):
    message = "Неизвестная ошибка"


class NotEnoughSpace(BaseError):
    message = "Недостаточно места"


class NotEnoughAmount(BaseError):
    message = "Недостаточно товара"


class UnknownTitle(BaseError):
    message = "Неизвестный товар"
