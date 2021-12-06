import pandas as pd
import yfinance as yf


class GetStock:
    def __init__(self, ticker: str, period: str, interval: str):
        self.ticker = ticker
        self.period = period
        self.interval = interval
        self.data = None

    def locate(self):
        try:
            if self.data is None:
                self.data = yf.download(
                    tickers=self.ticker, period=self.period, interval=self.interval
                )

        except Exception:
            raise Exception

        return self.data
