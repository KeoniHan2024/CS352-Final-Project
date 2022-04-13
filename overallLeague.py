from argparse import FileType
from tkinter.filedialog import asksaveasfile, asksaveasfilename
import pandas as pd
import numpy as np
from sklearn import linear_model
import requests
from nba_api.stats import endpoints
from matplotlib import pyplot as plt

import tkinter as tk
from tkinter import messagebox

# Class imports
from gui import *

""" This method gets a value from the drop down box and finds the specific method to call,
    if there is nothing selected it will show an error.
Args:
    playerName (String): the specified player that will be annotated in the graph
    typeOfStat (String): the specific data comparison it will be choosing
"""
def statChooser(playerName, typeOfStat):
    if typeOfStat == 'Field Goals Attempted vs. Points per Game':
        fga_vs_ppg(playerName)
        return
    elif typeOfStat == 'Field Goal % vs. Points per Game':
        fgp_vs_ppg(playerName)
        return
    elif typeOfStat == '3 Point Field Goals Attempted vs. Points per Game':
        tpfga_vs_ppg(playerName)
        return
    else:
        messagebox.showerror(
            title="No stat comparison chosen", 
            message="Please select a stat comparison in the drop box")
        return

def tpfga_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    x,y = df.FG3A, df.PTS

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    plt.scatter(x, y, s=15, alpha=.5)                                                   # Scatterplot:  Specfiy size(s) and transparency(alpha) of dots
    plt.title('NBA - Relationship Between 3-Point FG Attempted and Total Points')       # Give it a title
    plt.xlabel('Total 3-Point Field Goals Attempted')                                   # Label x-axis
    plt.ylabel('Total Points')                                                          # Label y-axis

    if playerName == "":
        plt.show()
        return

    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    plt.annotate(df.PLAYER[index[0]],                       # This the name of the top scoring player. Refer to the .head() from earlier
        (x[index[0]], y[index[0]]),                         # This is the point we want to annotate.  
        (x[index[0]],y[index[0]]-5),                        # These are coords for the text
        arrowprops=dict(arrowstyle='-'))                    # Here we use a flat line for the arrow '-'
    plt.show()
    plt.clf()
    return

def fgp_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    x,y = df.FG_PCT, df.PTS

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    plt.scatter(x, y, s=15, alpha=.5)                                       # Scatterplot:  Specfiy size(s) and transparency(alpha) of dots
    plt.title('NBA - Relationship Between FG % and Total Points')           # Give it a title
    plt.xlabel('Field Goal Percentage')                                     # Label x-axis
    plt.ylabel('Total Points')                                              # Label y-axis

    if playerName == "":
        plt.show()
        return

    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    plt.annotate(df.PLAYER[index[0]],                       # This the name of the top scoring player. Refer to the .head() from earlier
        (x[index[0]], y[index[0]]),                         # This is the point we want to annotate.  
        (x[index[0]]-2,y[index[0]]),                        # These are coords for the text
        arrowprops=dict(arrowstyle='-'))                    # Here we use a flat line for the arrow '-'
    plt.show()
    plt.clf()
    return


def fga_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    print(df)
    x,y = df.FGA/df.GP, df.PTS/df.GP

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    # Creates a linear regression using FGA and PPG as x and y axis
    model = linear_model.LinearRegression()
    model.fit(x,y)

    r2 = round(model.score(x,y), 2 )
    predicted_y = model.predict(x)

    # Now, lets make a plot with matplot lib using a iterative approach (which is easy to read)

    plt.scatter(x, y, s=15, alpha=.5)                            # Scatterplot:  Specfiy size(s) and transparency(alpha) of dots
    plt.plot(x, predicted_y, color = 'black')                    # line: Add line for regression line w/ predicted values
    plt.title('NBA - Relationship Between FGA and PPG')          # Give it a title
    plt.xlabel('FGA per Game')                                   # Label x-axis
    plt.ylabel('Points Per Game')                                # Label y-axis
    plt.text(10,25, f'R2={r2}')                                  # 10, 25 are the coordinates for our text. Adjust accordingly

    if playerName == "":
        plt.show()
        return

    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    plt.annotate(df.PLAYER[index[0]],                       # This the name of the top scoring player. Refer to the .head() from earlier
        (x[index[0]], y[index[0]]),                         # This is the point we want to annotate.  
        (x[index[0]]-3,y[index[0]]-2),                      # These are coords for the text
        arrowprops=dict(arrowstyle='-'))                    # Here we use a flat line for the arrow '-'
    plt.show()
    plt.clf()
    return
