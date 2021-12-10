from __future__ import annotations
from utils.stocks import GetStock
from utils.plotting import Plot, PlotComparison


class Ticker:
    def __init__(self, ticker: str):
        self.ticker = ticker
        self.df = None
        self.plot = None
        self.compare_plot = None

    def __eq__(self, other):
        return self.ticker == other.ticker

    def find_dataframe(self, trange: str = "1d", interval: str = "30m"):
        get_ticker = GetStock(self.ticker, trange, interval)
        self.df = get_ticker.locate()

        return self.df

    def plot_analysis(self, kind: str = "plot", argument="Close", condnl_args=None):
        self.plot = Plot()
        self.df = self.find_dataframe(*condnl_args)
        if self.df is not None:
            self.plot.initialize_settings(kind = kind)
            return self.plot.draw(
                self.df, self.ticker, kind, argument
            )  # return a base64 image of the analysis plot.
        else:
            raise Exception("No DataFrame Selected.")

    def compare(
        self, other_ticker: Ticker, condnl_args, argument="Close", plot_type="norm-plot"
    ):
        self.plot = PlotComparison()
        self.df = self.find_dataframe(*condnl_args)
        other_ticker.df = other_ticker.find_dataframe(*condnl_args)

        if (not (self.df).empty) and (not (other_ticker.df).empty):
            if plot_type == "norm-plot":
                return self.plot.linear_compare(
                    self.df, other_ticker.df, self.ticker, other_ticker.ticker, argument
                )
            elif plot_type == "reg-compare":
                return self.plot.regplot_compare(
                    self.df, other_ticker.df, self.ticker, other_ticker.ticker, argument
                )
            elif plot_type == "kde-compare":
                return self.plot.kde_compare(
                    self.df, other_ticker.df, self.ticker, other_ticker.ticker, argument
                )
        else:
            raise Exception("Invalid Ticker.")
