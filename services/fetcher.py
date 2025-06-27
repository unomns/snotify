import yfinance as yf

class StockFetcher:
    def get_current_price(self, symbol: str) -> float:
        ticker = yf.Ticker(symbol)
        price = ticker.info.get("regularMarketPrice")

        if price is None:
            raise ValueError(f"Price not available for symbol: {symbol}")
        
        return float(price)