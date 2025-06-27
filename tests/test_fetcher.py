from services.fetcher import StockFetcher


def test_fetch_sp500_price():
    fetcher = StockFetcher()
    price = fetcher.get_current_price("^GSPC")

    assert isinstance(price, float)
    assert price > 0
