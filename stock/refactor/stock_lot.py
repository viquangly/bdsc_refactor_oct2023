
from abc import ABC, abstractmethod
from datetime import datetime
import itertools
from typing import Optional, Tuple

from stock.refactor._typing import Numeric

tag_counter = itertools.count()


def _validate_date(date: str) -> str:
    try:
        valid_format = '%Y%m%d'
        valid_date = datetime.strptime(date, valid_format)
        return valid_date.strftime(valid_format)
    except Exception:
        raise ValueError("date must be a str in the form of 'YYYYMMDD'")


class StockLot(ABC):

    def __init__(
            self, stock: str, price: Numeric, quantity: Numeric, date: str,
            stop_loss: Optional[Numeric] = None, target: Optional[Numeric] = None
    ):
        self.stock = stock
        self.date = _validate_date(date)
        self.quantity = quantity
        self.price = price
        self.tag = next(tag_counter)
        self.stop_loss = None
        self.target = None

        self.set_stop_loss(stop_loss)
        self.set_target(target)

    @abstractmethod
    def set_stop_loss(self, stop_loss: Optional[Numeric]) -> None:
        pass

    @abstractmethod
    def set_target(self, target: Optional[Numeric]) -> None:
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_stock_tag(self):
        return self.tag

    def get_unique_id(self):
        return id(self)

    def get_face_value(self):
        return self.price * self.quantity

    def __hash__(self):
        return id(self)


class StockLotLong(StockLot):

    def set_stop_loss(self, stop_loss: Optional[Numeric]) -> None:
        self.stop_loss = 0.90 * self.price if stop_loss is None else stop_loss

    def set_target(self, target: Optional[Numeric]) -> None:
        self.target = 1.05 * self.price if target is None else target

    def __str__(self):
        return f'{self.stock}: Number of shares: {self.quantity} bought at {self.price}; Buy Date: {self.date}'


class StockLotShort(StockLot):

    def set_stop_loss(self, stop_loss: Optional[Numeric]) -> None:
        self.stop_loss = 1.05 * self.price if stop_loss is None else stop_loss

    def set_target(self, target: Optional[Numeric]) -> None:
        self.target = 0.98 * self.price if target is None else target

    def __str__(self):
        return f'{self.stock}: Number of shares: {self.quantity} Short at {self.price}; Buy Date: {self.date}'


class StockLotEMA(StockLotLong):

    def __init__(
            self, stock: str, price: Numeric, quantity: Numeric, date: str, ema: Tuple[Numeric, Numeric],
            stop_loss: Optional[Numeric] = None, target: Optional[Numeric] = None
    ):
        super().__init__(stock, price, quantity, date, stop_loss, target)
        self.ema_shorter, self.ema_longer = ema

    def get_ema(self) -> Tuple[Numeric, Numeric]:
        return self.ema_shorter, self.ema_longer
