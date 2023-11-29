import tkinter as tk
from tkinter import *

master = Tk()
Label(master, text = "First Name"). grid(row = 0)
Label(master, text = "Last Name"). grid(row = 1)
entry_1 = Entry(master)
entry_2 = Entry(master)
entry_1.grid(row = 0, column = 1)
entry_2.grid(row = 1, column = 1)
mainloop()
