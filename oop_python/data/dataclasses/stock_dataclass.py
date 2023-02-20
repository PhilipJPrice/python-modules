from dataclasses import make_dataclass, dataclass

Stock = make_dataclass("Stock", ("symbol", "current", "high", "low"))
stock = Stock("FB", 177.46, high=178.67, low=175.79)

class StockRegClass:
    def __init__(self, name, current, high, low):
        self.name = name
        self.current = current
        self.high = high
        self.low = low

stock_reg_class = StockRegClass("FB", 177.46, high=178.67, low=175.79)

@dataclass #@dataclass(order=True)
class StockDecorated:
    """
    Optional (default) parameters are in # comments
    """
    name: str
    current: float # = 0.0
    high: float # = 0.0
    low: float # = 0.0
