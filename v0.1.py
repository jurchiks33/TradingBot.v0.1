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
chart_label = ttk.Label(main_frame, text="Chart Area", 
                        background="gray", foreground="white")

#Control Buttons.
start_button = ttk.Button(main_frame, text="Start")
stop_button = ttk.Button(main_frame, text="Stop")
settings_button = ttk.Button(main_frame, text="Settings")
exit_button = ttk.Button(main_frame, text="Exit", command=root.destroy)


                        

