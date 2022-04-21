from argparse import FileType
import pandas as pd
import numpy as np
from sklearn import linear_model
from nba_api.stats import endpoints
from matplotlib import pyplot
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

""" This method gets a string for a player name and compares the three point field goals attempted vs 
    the leagues points per game. To see how they corelate
Args:
    playerName (String): the specified player that will be annotated in the graph
"""
def tpfga_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    x,y = df.FG3A, df.PTS

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    pyplot.scatter(x, y, s=15, alpha=.5)                                                   # Specifies the plot type
    pyplot.title('NBA - Relationship Between 3-Point FG Attempted and Total Points')       # Title
    pyplot.xlabel('Total 3-Point Field Goals Attempted')                                   # x-axis label
    pyplot.ylabel('Total Points')                                                          # y-axis label

    if playerName == "":
        pyplot.show()
        return

    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    pyplot.annotate(df.PLAYER[index[0]],                       # Index to name the player
        (x[index[0]], y[index[0]]),                         # Index to point to that player 
        (x[index[0]],y[index[0]]-5),                        # Coordinates to place the text
        arrowprops=dict(arrowstyle='-'))                    # type of line to draw towards point
    pyplot.show()
    pyplot.clf()
    return

""" This method gets a string for a player name and compares the field goal percentage vs 
    the leagues points per game. To see how they corelate
Args:
    playerName (String): the specified player that will be annotated in the graph
"""
def fgp_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    x,y = df.FG_PCT, df.PTS

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    pyplot.scatter(x, y, s=15, alpha=.5)                                       # Specifies the plot type
    pyplot.title('NBA - Relationship Between FG % and Total Points')           # Title
    pyplot.xlabel('Field Goal Percentage')                                     # x-axis label
    pyplot.ylabel('Total Points')                                              # y-axis label

    if playerName == "":
        pyplot.show()
        return

    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    pyplot.annotate(df.PLAYER[index[0]],                       # Index to name the player
        (x[index[0]], y[index[0]]),                         # Index to point to that player 
        arrowprops=dict(arrowstyle='-'))                    # type of line to draw towards point
    pyplot.show()
    pyplot.clf()
    return

""" This method gets a string for a player name and compares the total field goal attempted vs 
    the leagues points per game. To see how they corelate
Args:
    playerName (String): the specified player that will be annotated in the graph
"""
def fga_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
    print(df)
    x,y = df.FGA/df.GP, df.PTS/df.GP

    x = np.array(x).reshape(-1,1)
    y = np.array(y).reshape(-1,1)

    # creates the linear regression line
    linearLine = linear_model.LinearRegression()
    linearLine.fit(x,y)

    r2 = round(linearLine.score(x,y), 4)
    predicted_y = linearLine.predict(x)


    pyplot.scatter(x, y, s=15, alpha=.5)                            
    pyplot.plot(x, predicted_y, color = 'black')                   
    pyplot.title('NBA - Relationship Between FGA and PPG')          
    pyplot.xlabel('FGA per Game')                                  
    pyplot.ylabel('Points Per Game')                                
    pyplot.text(10,25, f'R2={r2}')                                  # labels the linear coorelation

    if playerName == "":
        pyplot.show()
        return

    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    pyplot.annotate(df.PLAYER[index[0]],                       # Index to name the player
        (x[index[0]], y[index[0]]),                           # Index to point to that player 
        (x[index[0]]-3,y[index[0]]-2),                     # Coordinates to place the text
        arrowprops=dict(arrowstyle='-'))                   # type of line to draw towards point
    pyplot.show()
    pyplot.clf()
    return
