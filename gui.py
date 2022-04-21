import tkinter as tk
from statAnalysis import *

"""show_frame 

    Description:
        puts the specified frame on top or shows it to the user
    Args:
        newFrame (tkinterFrame): tkinter frame that you want to show on top
"""
def show_frame(newFrame):
    newFrame.tkraise()

def callStatChoose(event):
    statChooser(name_var.get(), clicked.get())

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
# mainMenuFrame_PG_btn = tk.Button(mainMenuFrame, text = 'Analyze Per Game Stats', font=('orbitron', 15), command=lambda:show_frame(perGameFrame))
# mainMenuFrame_PG_btn.config(height = 5, width=50)
# mainMenuFrame_PG_btn.pack()

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
clicked = tk.StringVar()
measureableStats = [
    "Field Goals Attempted vs. Points per Game",
    "Field Goal % vs. Points per Game",
    "3 Point Field Goals Attempted vs. Points per Game"
]
    # Titles
overallLeague_title = tk.Label(overallLeagueFrame, text = 'Overall League Analysis', font=('orbitron', 25))
overallLeague_title.pack(fill='x')

    # Option Menus
drop = tk.OptionMenu(overallLeagueFrame , clicked, *measureableStats)
drop.pack()

    # Buttons
overallLeague_calc_btn = tk.Button(overallLeagueFrame, text = 'Analyze', font=('orbitron', 15), command=lambda:statChooser(name_var.get(), clicked.get()))
overallLeague_calc_btn.pack()

overallLeague_back_btn = tk.Button(overallLeagueFrame, text = 'Back', font=('orbitron', 10), command=lambda:show_frame(mainMenuFrame))
overallLeague_back_btn.pack()

    # Entries
overallLeague_name_entry = tk.Entry(overallLeagueFrame, textvariable=name_var)
overallLeague_name_entry.bind('<Return>', callStatChoose)
overallLeague_name_entry.pack()

window.mainloop()