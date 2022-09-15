from binance.spot import Spot as Client


class M2bot_binance:

    def __init__(self, market:str):
        self.market = market
        spot_client = Client(base_url="https://api.binance.com")
        #spot_client.avg_price()
        print(spot_client.book_ticker(self.market))


