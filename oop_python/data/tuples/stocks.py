import datetime

def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)

mid_value, date = middle(
    ("FB", 177.46, 178.67, 175.79), datetime.date(2023, 2, 18)
)
