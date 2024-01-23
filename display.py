import tkinter as tk
from tkinter import ttk

def create_main_window():
    root = tk.Tk()
    root.title("Trading Bot")

    #Screen width and height.
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    #taking 50% of screen height and width.
    window_width = screen_width // 2
    window_height = screen_height // 2

    #Centering window.
    center_x = screen_width // 4
    center_y = screen_height // 4

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    return root