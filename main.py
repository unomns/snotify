from services.fetcher import StockFetcher

def main():
    l = StockFetcher()
    price = l.get_current_price("^GSPC")
    print(f"S&P500 price is: ${price}")

main()
