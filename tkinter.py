import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as box
window = tk.Tk() 
window.title('Select Calculation')
window.pack(padx = 0, pady = 100)
button1 = tk.Button(window)
button1.configure(text = 'Mean', command = file)
button1.pack(side = LEFT)
button2 = tk.Button(window)
button2.configure(text = 'Median', command = file)
button2.pack()
button3 = tk.Button(window)
button3.configure(text = 'Mode', command = file)
button3.pack(side = RIGHT)
def file():
    window2 = tk.Tk()
    window2.pack(padx = 50, pady = 100)
    window2.title('Enter Directory')
    button4 = tk.Button(window2)
    button4.configure(text = 'Choose file', command = destroy)
    button4.pack(side = RIGHT)
    frame = tk.Frame(window2)
    entry = tk.Entry(frame)
    if not entry.get() == '*.xlsx' or not entry.get() == '*.csv' or not entry.get() == '*.xls':
        box.showerror('No Support', 'File type not supported')
