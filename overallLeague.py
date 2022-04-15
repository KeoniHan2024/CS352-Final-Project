from argparse import FileType
import pandas as pd
import numpy as np
from sklearn import linear_linearLine
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

    plt.scatter(x, y, s=15, alpha=.5)                                                   # Specifies the plot type
    plt.title('NBA - Relationship Between 3-Point FG Attempted and Total Points')       # Title
    plt.xlabel('Total 3-Point Field Goals Attempted')                                   # x-axis label
    plt.ylabel('Total Points')                                                          # y-axis label

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

    plt.annotate(df.PLAYER[index[0]],                       # Index to name the player
        (x[index[0]], y[index[0]]),                         # Index to point to that player 
        (x[index[0]],y[index[0]]-5),                        # Coordinates to place the text
        arrowprops=dict(arrowstyle='-'))                    # type of line to draw towards point
    plt.show()
    plt.clf()
    return

def fgp_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    x,y = df.FG_PCT, df.PTS

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    plt.scatter(x, y, s=15, alpha=.5)                                       # Specifies the plot type
    plt.title('NBA - Relationship Between FG % and Total Points')           # Title
    plt.xlabel('Field Goal Percentage')                                     # x-axis label
    plt.ylabel('Total Points')                                              # y-axis label

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

    plt.annotate(df.PLAYER[index[0]],                       # Index to name the player
        (x[index[0]], y[index[0]]),                         # Index to point to that player 
        arrowprops=dict(arrowstyle='-'))                    # type of line to draw towards point
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

    # creates the linear regression line
    linearLine = linear_linearLine.LinearRegression()
    linearLine.fit(x,y)

    r2 = round(linearLine.score(x,y), 2 )
    predicted_y = linearLine.predict(x)


    plt.scatter(x, y, s=15, alpha=.5)                            
    plt.plot(x, predicted_y, color = 'black')                   
    plt.title('NBA - Relationship Between FGA and PPG')          
    plt.xlabel('FGA per Game')                                  
    plt.ylabel('Points Per Game')                                
    plt.text(10,25, f'R2={r2}')                                  # labels the linear coorelation

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

    plt.annotate(df.PLAYER[index[0]],                       # Index to name the player
        (x[index[0]], y[index[0]]),                           # Index to point to that player 
        (x[index[0]]-3,y[index[0]]-2),                     # Coordinates to place the text
        arrowprops=dict(arrowstyle='-'))                   # type of line to draw towards point
    plt.show()
    plt.clf()
    return
