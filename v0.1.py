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

start_button.grid(row=1, column=0, padx=5, pady=5)
stop_button.grid(row=1, column=1, padx=5, pady=5)
settings_button.grid(row=1, column=2, padx=5, pady=5)
exit_button.grid(row=1, column=3, padx=5, pady=5)

#Log Section.
log_label = ttk.Label(main_frame, text="Log Section", 
                      background="black", foreground="white")
log_label.grid(row=2, column=0, columnspan=4, 
               sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)


                        

