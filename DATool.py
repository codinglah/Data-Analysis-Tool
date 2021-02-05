import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter.messagebox import *
def check():
    global df
    if '.csv' not in entry.get() and '.xlsx' not in entry.get() and '.xls' not in entry.get():
        showerror('No Support', 'File type not supported')
    else:
        try:
            df = pd.read_csv(entry.get())
        except:
            try:
                df = pd.read_excel(entry.get())
            except:
                showerror('No File', 'File not found. Please try again.')
            else:
                showinfo('Success', 'Success!')
                if types == 'plain':
                    t()
                else:
                    p()
        else:
            showinfo('Success', 'Success!')
            if types == 'plain':
                t()
            else:
                p()
def file():
    global window2, button4, frame, entry
    window2 = tk.Tk()
    window2.title('Enter Directory')
    window2.resizable(0, 0)
    button4 = tk.Button(window2)
    button4.configure(text = 'Choose file', command = check)
    button4.pack(side = tk.RIGHT)
    frame = tk.Frame(window2)
    entry = tk.Entry(frame)
    frame.pack(side = tk.LEFT)
    entry.pack(side = tk.LEFT)
def mean():
    global types
    types = 'mean'
    file()
def median():
    global types
    types = 'median'
    file()
def mode():
    global types
    types = 'mode'
    file()
def plain():
    global types
    types = 'plain'
    file()
def line():
    try:
        values = list(entry2.get().split(','))
        if len(values) == len(list(df.columns.values)):
            for value in values:
                df[value].plot()
        else:
            df.plot()
        plt.show()
    except ValueError:
        showerror('No Support', 'Oops! There appears to be unsupported data in your dataset. Please remove them and try again.')
def bar():
    try:
        values = list(entry2.get().split(','))
        if len(values) == len(list(df.columns.values)):
            for value in values:
                df[value].plot(kind = "bar")
        else:
            df.plot(kind = "bar")
        plt.show()
    except ValueError:
        showerror('No Support', 'Oops! There appears to be unsupported data in your dataset. Please remove them and try again.')
def hist():
    global window5
    window5 = tk.Tk()
    window5.resizable(0, 0)
    label2 = tk.Label(window5, text = "Please enter comma-separated columns or 'NIL' for all columns:")
    label2.grid(row = 1, column = 3)
    frame2 = tk.Frame(window5)
    entry2 = tk.Entry(frame)
    frame2.pack(side = tk.LEFT)
    entry2.pack(side = tk.LEFT)
    try:
        values = list(entry2.get().split(','))
        if len(values) == len(list(df.columns.values)):
            for value in values:
                df[value].hist()
        else:
            df.hist()
        plt.show()
    except ValueError:
        showerror('No Support', 'Oops! There appears to be unsupported data in your dataset. Please remove them and try again.')
def pie():
    global window5
    window5 = tk.Tk()
    window5.resizable(0, 0)
    label2 = tk.Label(window5, text = "Please enter comma-separated labels or 'NIL' for no label:")
    label2.grid(row = 1, column = 3)
    frame2 = tk.Frame(window5)
    entry2 = tk.Entry(frame)
    frame2.pack(side = tk.LEFT)
    entry2.pack(side = tk.LEFT)
    try:
        values = list(entry2.get().split(','))
        if len(values) == len(list(df.columns.values)):
            plt.pie(df, labels = values)
        elif entry2.get() == "NIL":
            plt.pie(df)
        else:
            plt.pie(df, labels = df.columns.values)
        plt.show()
    except ValueError:
        showerror('No Support', 'Oops! There appears to be unsupported data in your dataset. Please remove them and try again.')
def t():
    global window3, button5, button6, button8, button9
    window3 = tk.Tk()
    window3.title('Select Type')
    window3.resizable(0, 0)
    label2 = tk.Label(window3, text = 'Select Type of Graph:')
    label2.grid(row = 1, column = 10)
    button5 = tk.Button(window3)
    button5.configure(text = 'Line', command = line)
    button5.grid(row = 2, column = 1)
    button6 = tk.Button(window3)
    button6.configure(text = 'Bar', command = bar)
    button6.grid(row = 2, column = 4)
    button8 = tk.Button(window3)
    button8.configure(text = 'Hist', command = hist)
    button8.grid(row = 2, column = 12)
    button9 = tk.Button(window3)
    button9.configure(text = 'Pie', command = pie)
    button9.grid(row = 2, column = 16)
def p():
    global window4
    window4 = tk.Tk()
    window4.title((types, 'calculation results'))
    try:
        if types == 'mean':
            label3 = tk.Label(window4, text = (df.columns.values, '\n\n', df.mean()))
        elif types == 'median':
            label3 = tk.Label(window4, text = (df.columns.values, '\n\n', df.median()))
        else:
            label3 = tk.Label(window4, text = (df.columns.values, '\n\n', df.mode()))
    except:
        showerror('No Support', 'Oops! There appears to be unsupported data in your dataset. Please remove them and try again.')
    label3.grid(row = 1)
window = tk.Tk()
window.title('Select Calculation')
window.resizable(0, 0)
label = tk.Label(window, text = 'Data Analysis Tool v1.0.0-a3')
label.grid(row = 1, column = 6)
button1 = tk.Button(window)
button1.configure(text = 'Mean', command = mean)
button1.grid(row = 3, column = 1)
button2 = tk.Button(window)
button2.configure(text = 'Median', command = median)
button2.grid(row = 3, column = 4)
button3 = tk.Button(window)
button3.configure(text = 'Mode', command = mode)
button3.grid(row = 3, column = 8)
button7 = tk.Button(window)
button7.configure(text = 'Plain', command = plain)
button7.grid(row = 3, column = 12)
window.mainloop()
try:
    if types:
        window2.mainloop()
    elif types == 'plain':
        window4.mainloop()
    else:
        window3.mainloop()
        window5.mainloop()
except:
    pass
