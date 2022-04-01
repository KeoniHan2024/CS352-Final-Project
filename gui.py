# import pandas as pd
# import numpy as np
# from sklearn import linear_model
# import requests
# from nba_api.stats import endpoints
# from matplotlib import pyplot as plt
import tkinter as tk
from overallLeague import *

"""show_frame 

    Description:
        puts the specified frame on top or shows it to the user
    Args:
        newFrame (tkinterFrame): tkinter frame that you want to show on top
"""
def show_frame(newFrame):
    newFrame.tkraise()

# Initializes the window and the main menu frame
window = tk.Tk()
window.state('zoomed')
window.title('Basketball Statistics Analyzer')

window.rowconfigure(0, weight=1)
window.columnconfigure(0, weight=1)

mainMenuFrame = tk.Frame(window)
perGameFrame = tk.Frame(window)
overallLeagueFrame = tk.Frame(window)

#Goes through each frame and puts them in the window
for frame in (mainMenuFrame, perGameFrame, overallLeagueFrame):
    frame.grid(row=0,column=0,sticky='nsew')

# Makes main menu frame visible at launch
show_frame(mainMenuFrame)

#=========== Main Menu Frame Code ==============
    # Titles
mainMenuFrame_title = tk.Label(mainMenuFrame, text = 'Main Menu', font=('orbitron', 25))
mainMenuFrame_title.pack(fill='x')

    # Buttons
mainMenuFrame_PG_btn = tk.Button(mainMenuFrame, text = 'Analyze Per Game Stats', font=('orbitron', 15), command=lambda:show_frame(perGameFrame))
mainMenuFrame_PG_btn.config(height = 5, width=50)
mainMenuFrame_PG_btn.pack()

mainMenuFrame_OVRLL_btn = tk.Button(mainMenuFrame, text = 'Overall League Analysis',font=('orbitron', 15), command=lambda:show_frame(overallLeagueFrame))
mainMenuFrame_OVRLL_btn.config(height = 5, width=50)
mainMenuFrame_OVRLL_btn.pack()

mainMenuFrame_QT_btn = tk.Button(mainMenuFrame, text='QUIT', font=('orbitron', 15), command=window.destroy)
mainMenuFrame_QT_btn.pack()
#=========== Per Game Frame Code ==============
    # Titles
perGameFrame_title = tk.Label(perGameFrame, text = 'Per Game Player Analysis', font=('orbitron', 25))
perGameFrame_title.pack(fill='x')

    # Buttons
perGameFrame_back_btn = tk.Button(perGameFrame, text = 'Back', font=('orbitron', 10), command=lambda:show_frame(mainMenuFrame))
perGameFrame_back_btn.pack()

#=========== Overall League Frame Code ==============
    #Instances
name_var=tk.StringVar()

    # Titles
overallLeague_title = tk.Label(overallLeagueFrame, text = 'Overall League Analysis', font=('orbitron', 25))
overallLeague_title.pack(fill='x')

    # Buttons
overallLeague_back_btn = tk.Button(overallLeagueFrame, text = 'Back', font=('orbitron', 10), command=lambda:show_frame(mainMenuFrame))
overallLeague_back_btn.pack()

overallLeague_calc_btn = tk.Button(overallLeagueFrame, text = 'Analyze', font=('orbitron', 15), command=lambda:fga_vs_ppg(name_var.get()))
overallLeague_calc_btn.pack()

overallLeague_save_btn = tk.Button(overallLeagueFrame, text = 'Save Graph', font=('orbitron', 15), command=lambda:savePlot())
overallLeague_save_btn.pack()

    # Entries
overallLeague_name_entry = tk.Entry(overallLeagueFrame, textvariable=name_var)
overallLeague_name_entry.pack()



# # Here we access the leagueleaders module through endpoints & assign the class to "data"
# data = endpoints.leagueleaders.LeagueLeaders() 

# # Our "data" variable now has built in functions such as creating a dataframe for our data
# # df = data.league_leaders.get_data_frame()
# df = data.league_leaders.get_data_frame()
# # test

# # First we need to get per game stats.
# # We divide each variable by games played (GP) to get per game average
# x, y = df.FGA/df.GP, df.PTS/df.GP 

# # we have to reshape our array from 1d to 2d. 
# # The proper shaped array is an input requirement for the linear model
# # reshaping is usually an issue when using 1 x variable
# x = np.array(x).reshape(-1,1)     
# y = np.array(y).reshape(-1,1)     



# """ Build and fit linea regression model """
# # create an object that contains the linear model class
# # Fit our modeling using FGA (x) and PPG (y)
# model = linear_model.LinearRegression()    
# model.fit(x,y)                             

# # Get our r2 value and round it to 2 decimals. How much variance is exaplained?
# # Get our predicted y values for x
# r2 = round(model.score(x,y), 2)            
# predicted_y = model.predict(x)     

# # Now, lets make a plot with matplot lib using a iterative approach (which is easy to read)

# plt.scatter(x, y, s=15, alpha=.5)                            # Scatterplot:  Specfiy size(s) and transparency(alpha) of dots
# plt.plot(x, predicted_y, color = 'black')                    # line: Add line for regression line w/ predicted values
# plt.title('NBA - Relationship Between FGA and PPG')          # Give it a title
# plt.xlabel('FGA per Game')                                   # Label x-axis
# plt.ylabel('Points Per Game')                                # Label y-axis
# plt.text(10,25, f'R2={r2}')                                  # 10, 25 are the coordinates for our text. Adjust accordingly

# name = input("Which player do you want to highlight on the regression model?")
# index = df.index[df['PLAYER']==name].to_list()

# plt.annotate(df.PLAYER[index[0]],                       # This the name of the top scoring player. Refer to the .head() from earlier
#              (x[0], y[0]),                       # This is the point we want to annotate.  
#              (x[0]-7,y[0]-2),                    # These are coords for the text
#              arrowprops=dict(arrowstyle='-'))    # Here we use a flat line for the arrow '-'


# # Finally, let's save an image called 'graph.png'. 
# # We'll set the dpi (dots per inch) to 300, so we have a nice looking picture.
# plt.show()

