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

global lastPlot

def fga_vs_ppg(playerName):
    data = endpoints.LeagueLeaders()
    df = data.league_leaders.get_data_frame()
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

    
    # name = input("Which player do you want to highlight on the regression model?")
    playerName = playerName.title()
    index = df.index[df['PLAYER']==playerName].to_list()

    if not index:
        messagebox.showerror(
            title="Invalid Player Name", 
            message="Please type in a valid NBA player")
        return

    plt.annotate(df.PLAYER[index[0]],                       # This the name of the top scoring player. Refer to the .head() from earlier
        (x[0], y[0]),                       # This is the point we want to annotate.  
        (x[0]-7,y[0]-2),                    # These are coords for the text
        arrowprops=dict(arrowstyle='-'))    # Here we use a flat line for the arrow '-'
    plt.show()
    plt.clf()
    return

def savePlot():
    # files = [("png file","*.png")]
    if not plt:
        messagebox.showerror(
            title="Can't Save File", 
            message="No Graph to Save")
        return
