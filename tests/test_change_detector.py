from models.stock import Stock
from services.change_detector import PriceChangeDetector


def test_detects_change_on_new_symbol():
    old = None
    new = Stock(symbol="APPL", price=150.0)

    result = PriceChangeDetector.has_changed(old, new)

    assert result is True


def test_detects_price_change():
    old = Stock(symbol="APPL", price=150.0)
    new = Stock(symbol="AAPL", price=151.0)

    result = PriceChangeDetector.has_changed(old, new)

    assert result is True


def test_detects_no_change():
    old = Stock(symbol="APPL", price=150.0)
    new = Stock(symbol="AAPL", price=150.0)

    result = PriceChangeDetector.has_changed(old, new)

    assert result is False
