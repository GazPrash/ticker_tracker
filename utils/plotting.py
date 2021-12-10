from __future__ import annotations
import pandas as pd
import random as rd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


class Plot:
    def __init__(self):
        self.plt = plt
        self.sns = sns

    def initialize_settings(self, kind):
        if kind == "cluster" or kind == "joint":
            # this plots do not allow to change the default figsize orientation, 
            # hence by doing so it'll result in a new stack added to matplotlib axes, 
            # which will output an extra empty figure
            return
        else:
            self.plt.figure(figsize=(8, 4))
            self.sns.set_context("notebook")

    def random_ink(self):
        rgb_colors = (
            rd.randint(0, 255),
            rd.randint(0, 255),
            rd.randint(0, 255),
        )

        return "#" + "".join("%02x" % i for i in rgb_colors)

    def draw(self, df: pd.DataFrame, title: str, kind: str = "plot", argument="Close"):
        clr = self.random_ink()
        # df.index = df.index.strftime('%d,%b|%H:%M')

        if kind == "joint":
            arg1, arg2 = argument.split(" ")
        else:
            argument = argument.strip()

        if kind == "plot":
            self.plt.plot(
                df.index,
                df[argument],
                linewidth="2",
                color=clr,
                label=title,
                marker="H",
            )
            self.plt.ylabel(argument)
            # self.plt.xticks(ticks = df.index, labels = pd.Series(df.index.strftime('%d,%b|%H:%M')), rotation = '45', fontsize =5)
            self.plt.title(f"{title}-{argument}")

        elif kind == "bar":
            self.plt.bar(df.index, df[argument], color=clr, label=title)
            self.plt.ylabel(argument)
            # self.plt.xticks(ticks = df.index, labels = df.index.strftime('%d,%b|%H:%M'))
            self.plt.title(f"{title}-{argument}")

        elif kind == "reg":
            self.sns.regplot(
                np.arange(len(df), dtype="int"),
                df[argument],
                color=clr,
                label=title,
                marker="*",
            )
            self.plt.ylabel(argument)
            # self.plt.xticks([])
            self.plt.title(f"{title}-{argument}")

        elif kind == "vio" or kind == "vios" or kind == "box" or kind == "kde":
            if kind == "vio" or kind == "vios":
                swarm = True if (kind == "vios") else False
                self.violin_plot(df, title, argument, swarm=swarm)

            elif kind == "box":
                self.box_plot(df, title, argument)

            elif kind == "kde":
                self.kernal_density_plot(df, title, argument)

        elif kind == "ecdf":
            self.ecdf_plot(df, title, argument)

        elif kind == "joint":
            self.joint_plot(df, title, argument1=arg1, argument2=arg2)

        elif kind == "cluster":
            self.cluster_map(df, title)

        self.plt.show()

    def ecdf_plot(self, df: pd.Dataframe, title: str, argument: str = "Close"):
        clr = self.random_ink()
        self.sns.ecdfplot(x=df[argument], color=clr, linewidth="2")
        self.plt.xlabel(title)
        self.plt.title(f"Empirical Cumulative Dist. Function for {title}")

    def violin_plot(
        self, df: pd.Dataframe, title: str, argument: str = "Close", swarm=False
    ):
        clr = self.random_ink()
        self.sns.violinplot(x=None, y=argument, data=df, color=clr)
        if swarm:
            self.sns.swarmplot(x=None, y=argument, data=df, color="#000")
        self.plt.title(f"Violin Dist. for {title}")

    def box_plot(self, df: pd.Dataframe, title: str, argument: str = "Close"):
        clr = self.random_ink()
        self.sns.boxplot(x=None, y=argument, data=df, color=clr)
        self.plt.title(f"Box Dist. for {title}")

    def kernal_density_plot(
        self, df: pd.Dataframe, title: str, argument: str = "Close"
    ):
        clr = self.random_ink()
        self.sns.kdeplot(x=argument, y=None, data=df, color=clr)
        self.plt.title(f"Kernal Desnity Est. for {title}")

    def joint_plot(
        self,
        df: pd.Dataframe,
        title: str,
        argument1: str = "Close",
        argument2: str = "Open",
    ):
        clr = self.random_ink()
        self.sns.jointplot(x=argument1, y=argument2, data=df, color=clr, marker="H")
        self.plt.title(
            f"Joint Plot comparison for {title} - ({argument1} & {argument2})"
        )

    def cluster_map(
        self, df: pd.Dataframe, title: str
    ):
        self.sns.clustermap(data=df[["Close", "Adj Close", "Open", "High"]])
        self.plt.title(f"Cluster Map for {title}")

    def encode_img(
        self,
    ):
        ...  # TODO  Define Base64 transfer of image for API Calls...


class PlotComparison(Plot):
    def __init__(self):
        super().__init__()

    def linear_compare(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        title1: str,
        title2: str,
        argument: str = "Close",
    ):
        clr1 = self.random_ink()
        clr2 = self.random_ink()

        self.plt.plot(
            df1[argument], linewidth="2", marker="H", color=clr1, label=title1
        )
        self.plt.plot(
            df2[argument], linewidth="2", marker="*", color=clr2, label=title2
        )
        self.plt.legend()
        self.plt.title(f"{title1}-{title2} Comparison w/ Linear Plot")

        self.plt.show()

    def regplot_compare(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        title1: str,
        title2: str,
        argument: str = "Close",
    ):
        clr = self.random_ink()
        self.sns.regplot(df1[argument], df2[argument], color=clr)
        self.plt.xlabel(title1)
        self.plt.ylabel(title2)
        self.plt.title(f"{title1}-{title2} Comparison w/ Linear Regression")

        self.plt.show()

    def kde_compare(
        self,
        df1: pd.DataFrame,
        df2: pd.DataFrame,
        title1: str,
        title2: str,
        argument: str = "Close",
    ):
        clr1 = self.random_ink()
        clr2 = self.random_ink()
        self.sns.kdeplot(x=df1[argument], y=None, color=clr1, label=title1)
        self.sns.kdeplot(x=df2[argument], y=None, color=clr2, label=title2)
        self.plt.legend()
        self.plt.title(f"{title1}-{title2} Comparison w/ Kernal Density Estimation")

        self.plt.show()
