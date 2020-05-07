import tkinter as tk
import time
import os

def search_nba_players():
	var = entry.get()
	print(var)

def search_ncaa_players():
	var = entry.get()
	print(var)

if __name__ == '__main__':
	window = tk.Tk()
	window.title('Database System Project - Basketball')
	window.geometry('600x450')
	window.resizable(width=False, height=False)
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
	entry = tk.Entry(window, show=None, width=30)
	entry.pack()
	nba = tk.Button(window, text='Check on NBA players', width=30, height=2, command=search_nba_players)
	nba.pack()
	ncaa = tk.Button(window, text='Check on NCAA players', width=30, height=2, command=search_ncaa_players)
	ncaa.pack()
	window.mainloop()

