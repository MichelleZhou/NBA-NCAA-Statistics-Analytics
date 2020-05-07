import tkinter as tk
import time
import os
from queries import *

#function for Lookup NBA players button
def search_nba_players():
	var = entry.get()
	nba_player_lookup(var)

#function for Lookup NCAA players button
def search_ncaa_players():
	var = entry.get()
	ncaa_player_lookup(var)

#Main
if __name__ == '__main__':

	#Window setup
	window = tk.Tk()
	window.title('Database System Project - Basketball')
	window.geometry('600x450')
	window.resizable(width=False, height=False)

	#Menu gif
	image_file = [tk.PhotoImage(file='code/dear-basketball.gif', format='gif -index %i' %(i)) for i in range(9)]

	def update(ind):
		if ind == 9:
			ind = 0
		frame = image_file[ind]
		ind+=1
		label.configure(image=frame)
		window.after(1800, update, ind)
	label = tk.Label(window)
	label.pack()
	window.after(0, update, 0)

	#Menu entry
	entry = tk.Entry(window, show=None, width=30)
	entry.pack()

	#Menu button
	nba = tk.Button(window, text='Lookup NBA players', width=30, height=2, command=search_nba_players)
	nba.pack()
	ncaa = tk.Button(window, text='Lookup NCAA players', width=30, height=2, command=search_ncaa_players)
	ncaa.pack()
	window.mainloop()

