import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
import tkinter.messagebox as box
def check():
    if '.csv' not in entry.get() and '.xlsx' not in entry.get() and '.xls' not in entry.get():
        box.showerror('No Support', 'File type not supported')
    else:
        try:
            df = pd.read_csv(entry.get())
        except:
            try:
                df = pd.read_excel(entry.get())
            except:
                box.showerror('No File', 'File not found. Please try again.')
            else:
                box.showinfo('Success', 'Success!')
        else:
            box.showinfo('Success', 'Success!')
        
def file():
    global window2, button4, frame, entry
    window2 = tk.Tk()
    window2.title('Enter Directory')
    button4 = tk.Button(window2)
    button4.configure(text = 'Choose file', command = check)
    button4.pack(side = tk.RIGHT)
    frame = tk.Frame(window2)
    entry = tk.Entry(frame)
    frame.pack(side = tk.LEFT)
    entry.pack(side = tk.LEFT)
def mean():
    global type    
    type = 'mean'
    file()
def median():
    global type
    type = 'median'
    file()
def mode():
    global type
    type = 'mode'
    file()
window = tk.Tk()
window.title('Select Calculation')
label = tk.Label(window, text = 'Data Analysis Tool v1.0.0-a1')
label.grid(row = 1, column = 4)
button1 = tk.Button(window)
button1.configure(text = 'Mean', command = mean)
button1.grid(row = 2, column = 1)
button2 = tk.Button(window)
button2.configure(text = 'Median', command = median)
button2.grid(row = 2, column = 4)
button3 = tk.Button(window)
button3.configure(text = 'Mode', command = mode)
button3.grid(row = 2, column = 8)
window.mainloop()
window2.mainloop()
