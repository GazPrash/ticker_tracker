import pandas as pd
from utils.stocks import GetStock
from utils.plotting import Plot
from __future__ import annotations


class Ticker:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.df = None
        self.plot = Plot()

    def __eq__(self, other):
        return (self.df == other.df)

    def find_dataframe(self, trange: str, interval: str):
        get_ticker = GetStock(self.ticker, trange, interval)
        self.df = get_ticker.locate()

        return self.df

    def plot_analysis(self, kind: str = "plot", argument = 'Close'):
        if self.df is not None:
            return self.plot.draw(self.df, kind, argument)  # return a base64 image of the analysis plot.
        else:
            raise Exception("No DataFrame Selected.")

    def compare(self, other_ticker: Ticker, condnl_args, argument = 'Close'):
        if self.df is None:
            self.find_dataframe(condnl_args)
        if other_ticker.df is None:
            other_df = other_ticker.find_dataframe(condnl_args)
        if (not (self.df).empty) and (not (other_ticker.df).empty):
            return self.plot.draw_compare(self.df, other_ticker.df, argument)
        else:
            raise Exception("Invalid Ticker.")
