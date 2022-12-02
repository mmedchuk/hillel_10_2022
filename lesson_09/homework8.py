from dataclasses import dataclass
from json import loads
from pathlib import Path


@dataclass
class Price:
    amount: int
    currency: str

    def __add__(self, other: int) -> int:
        result_currency = "usd"

        if self.currency == other.currency:
            result = self.amount + other.amount
            result_currency = self.currency

        elif self.currency != "usd" and other.currency == "usd":
            result = self.amount * convert(self.currency) + other.amount

        elif self.currency == "usd" and other.currency != "usd":
            result = self.amount + other.amount * convert(other.currency)

        else:
            result = self.amount * convert(self.currency) + other.amount * convert(
                other.currency
            )

        return f"{round(result, 2)} {result_currency}"

    def __sub__(self, other: int) -> int:
        result_currency = "usd"

        if self.currency == other.currency:
            result = self.amount - other.amount
            result_currency = self.currency

        elif self.currency != "usd" and other.currency == "usd":
            result = self.amount * convert(self.currency) - other.amount

        elif self.currency == "usd" and other.currency != "usd":
            result = self.amount - other.amount * convert(other.currency)

        else:
            result = self.amount * convert(self.currency) - other.amount * convert(
                other.currency
            )

        return f"{round(result, 2)} {result_currency}"


class ExchangeRateProcessor:
    _isinstance = None
    _isinitialized = False

    def __new__(cls, *args, **kwargs):
        if cls._isinstance:
            return cls._isinstance
        cls._isinstance = super().__new__(cls)
        return cls._isinstance

    def __init__(self, filename: Path) -> None:
        if self._isinitialized:
            return
        self.path: Path = filename
        self._isinitialized = True

    def get_exchange_rates(self, currency: str) -> float:
        with open(self.path) as file:
            row_data = file.read()
            data = loads(row_data)
            for i in data["rates_to_usd"]:
                if currency == i["from_"]:
                    return i["index"]


PATH = Path(__file__).parent / "exchange_rates.json"

exchange_rate_processor = ExchangeRateProcessor(PATH)
convert = exchange_rate_processor.get_exchange_rates

a = Price(10, "usd")
b = Price(20, "uah")
print(a)
print(b)
print(a + b)
print(a - b)
