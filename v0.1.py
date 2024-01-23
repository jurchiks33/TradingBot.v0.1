import tkinter as tk
from tkinter import ttk

#Main window.
root = tk.Tk()
root.title("Trading Bot")

#Main frame.
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W,
                tk.E, tk.N, tk.S))

#Chart Area.


