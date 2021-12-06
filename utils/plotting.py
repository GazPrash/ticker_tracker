import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns
from __future__ import annotations


class Plot:
    def __init__(self):
        self.plt = plt
        self.sns = sns
        self.plt.figure(figsize = (15, 5))
        self.sns.set_context('notebook')

    def random_ink(self):
        rgb_colors = (
            rd.randint(0, 255),
            rd.randint(0, 255),
            rd.randint(0, 255),
        )

        return ('#' + ''.join('%02x'%i for i in rgb_colors))

    def draw(self, df: pd.DataFrame, title: str,  kind:str = 'plot', argument = 'Close'):
        clr = self.random_ink()

        if kind == 'plot':
            self.plt.plot(df.index, df[argument], linewidth = '2', marker = 'H', color = clr, label = title)
            self.plt.ylabel(argument)
            self.plt.title(f'{title}-{argument}')

        elif kind == 'bar':
            self.plt.bar(df.index, df[argument], color = clr, label = title)
            self.plt.ylabel(argument)
            self.plt.title(f'{title}-{argument}')
        
        elif kind == 'reg':
            self.sns.regplot(df.index, df[argument], color = clr, label = title)
            self.plt.ylabel(argument)
            self.plt.title(f'{title}-{argument}')

        elif kind == 'vio' or kind == 'vios' or kind == 'box' or kind == 'kde':
            pass    

        elif kind == 'ecdf':
            pass


    def draw_compare(self, df1: pd.DataFrame, df2: pd.DataFrame, title1, title2,  argument:str = 'Close'):
        clr1 = self.random_ink()
        clr2 = self.random_ink()

        self.plt.plot(df1[argument], linewidth = '2', marker = 'H', color = clr1, label = title1)
        self.plt.plot(df2[argument], linewidth = '2', marker = '*', color = clr2, label = title2)
        self.plt.legend()
        self.plt.title()

        return ...

    def regplot_compare(self, df1: pd.DataFrame, df2: pd.DataFrame, title1, title2,  argument:str = 'Close'):
        clr = self.random_ink()
        self.sns.regplot(df1[argument], df2[argument], color = clr)
        self.xlabel(title1)
        self.ylabel(title2)
        self.plt.title(f'{title1}-{title2} Comparison w/ Linear Regression')

        return ...

    def ecdfplot(self, df: pd.Dataframe, title, argument:str = 'Close'):
        clr = self.random_ink()
        self.sns.ecdfplot(x = df['argument'], color = clr, linewidth = '2')
        self.plt.xlabel(title)
        self.plt.title(f"Empirical Cumulative Dist. Function for {title}")



    def kernal_density_plots(self, swarm = False):
        pass

    def jointplt(self):
        pass
