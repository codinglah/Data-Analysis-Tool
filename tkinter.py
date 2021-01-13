import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
window = tk.Tk()
window.pack(padx = 0, pady = 100)
button1 = tk.Button(window)
button1.configure(text = 'Mean')
button1.pack(padx = 0, pady = 0)
button2 = tk.Button(window)
button2.configure(text = 'Median')
button2.pack(padx = 50, pady = 0)
button3 = tk.Button(window)
button3.configure(text = 'Mode')
button3.pack(padx = 100, pady = 0)
