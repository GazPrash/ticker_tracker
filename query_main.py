from __future__ import annotations
from tickers import Ticker


class TicQuery:
    def __init__(self, tic):
        self.tic = tic
        self.tic_obj = None
        self.mode = None
        self.query_type = 'self'

    def __eq__(self, other):
        return (self.tic == other.tic) & (self.tic_obj == other.tic_obj)

    def verify_mode(self, other):
        return self.mode == other.mode

    def set_qtype(self):
        perf:str = input('Do You wish to perform a comparison analysis b/w this ticker with another? (Y/n)')
        if perf.lower() == 'y':
            self.query_type = 'comparison'

    def get_qtype(self):
        return self.query_type

    def initialize(self):
        self.tic_obj = Ticker(self.tic)
        if (self.tic_obj.find_dataframe()).empty:
            raise Exception(
                "We do not have any information regarding the requested ticker/stock"
            )

    def set_mode(self):
        arg: str = input("Would you like to analyze the latest results? (Y/n): ")
        if arg.lower() == "y":
            t_range: str = "1d"
            interval: str = "30m"

        else:
            t_range: str = input(
                "Select & Enter a valid timeframe (1d/5d/1mo/3mo/1y/max)"
            )
            interval: str = input(
                "Select & Enter a valid time interval (5m/15m/30m/90m/1h/1d)"
            )

        self.mode = (t_range, interval)

    def operation(self):
        print(
            """
            1. Download CSV
            2. Analyze Data
        """
        )

        opt: int = int(
            input(
                "Please choose an option from above (Enter the index number of your choice): "
            )
        )

        if opt == 1:
            self.save_df()
        elif opt == 2:
            self.plot_normal()

    def save_df(self):
        df = self.tic_obj.find_dataframe(*self.mode)
        df.to_csv(f"Downloads/{self.tic} Stocks/")

    def plot_argument(self, self_compare: bool = False) -> str:
        arg_dict = {1: "Close", 2: "Open", 3: "High", 4: "Adj Close", 5: "Volume"}

        print(
            """
            1. Close
            2. Open
            3. Max
            4. Adjusted Close
            5. Volume 
        """
        )

        argument1: str = ""
        argument2: str = ""

        task1: int = int(
            input(
                "Please choose a category from above for analysis (Enter the index number of your choice): "
            )
        )
        argument1 = arg_dict[task1]

        if self_compare:
            task2: int = int(
                input(
                    "Please choose a category from above for analysis, for the 2nd curve in the joint plot (Enter the index number of your choice): "
                )
            )

            argument2 = arg_dict[task2]

        return argument1 + " " + argument2

    def plot_normal(self):
        print(
            """
            1. Line Plot
            2. Bar Plot
            3. Linear Regression Plot
            4. Violin Plot
            5. Violin Plot (w/ Swarm)
            6. Box Plot
            7. Empirical Cumulative Desnity Frequency Plot
            8. Joint Plot Comparison
        
        """
        )
        anls_mode: int = int(
            input(
                "Please choose an option from above (Enter the index number of your choice): "
            )
        )

        if anls_mode == 1:
            plot_style = "plot"
        elif anls_mode == 2:
            plot_style = "bar"
        elif anls_mode == 3:
            plot_style = "reg"
        elif anls_mode == 4:
            plot_style = "vio"
        elif anls_mode == 5:
            plot_style = "vios"
        elif anls_mode == 6:
            plot_style = "box"
        elif anls_mode == 7:
            plot_style = "ecdf"
        elif anls_mode == 8:
            plot_style = "joint"

        if anls_mode == 8:
            main_arg = self.plot_argument(self_compare=True)
        else:
            main_arg = self.plot_argument()

        plot_fig = self.tic_obj.plot_analysis(kind=plot_style, argument=(main_arg), condnl_args= self.mode)
        # plot_img.save(f"Downloads/{self.tic} Analysis")  # ......TODO Yet to define.


    def plot_compare(self, other: TicQuery):

        # if not self.verify_conditionals(other):
        #     #note to self : use logging for the love of god aaaaaaaaaaaaaaaaaaaaaah

        #     print(
        #         """You've opted to analyze two different tickers together with contradicting time 
        #         intervals and range. 
        #         [Initial Ticker's settings will be applied for this analysis].""",
        #     end = '\n\n')

        print(
            """
            1. Linear Plot Comparison
            2. Scatter Plot Comparison w/ Regression        
        
        """
        )
        ctype: int = int(
            input("Choose a Comparison Type (Enter the index number of your choice): ")
        )

        main_arg = self.plot_argument().strip()
        print(f"{self.mode}")
        if ctype == 1:
            self.tic_obj.compare(other.tic_obj, self.mode, argument = main_arg)
            # plot_img.save(f"Downloads/{self.tic} Analysis")  # ......TODO Yet to define.
        else:
            self.tic_obj.compare(other.tic_obj, self.mode, argument = main_arg, plot_type = 'reg-compare')



if __name__ == "__main__":
    tickr:str = input('Enter a Valid Stock Ticker: ')
    query1 = TicQuery(tickr)
    query1.initialize()
    query1.set_mode()
    query1.set_qtype()

    if query1.get_qtype() == "comparison":
        tickr2:str = input('Enter an another Valid Stock Ticker: ')
        query2 = TicQuery(tickr2)
        query2.initialize()

        query1.plot_compare(query2)
    else:
        query1.operation()



