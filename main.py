import config
from listener import Listener

def main():
    l = Listener(config.STOCK_URL, config.STOCK_PORT)
    l.listen()

main()