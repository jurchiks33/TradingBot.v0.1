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

    #Status information.
    status_label = ttk.Label(main_frame, 
                            text="Balance: $xxxxx | Open Positions: xx | Recent Trades: xxx")
    status_label.grid(row=3, column=0, columnspan=4)

    return root