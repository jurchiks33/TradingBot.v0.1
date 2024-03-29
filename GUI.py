import tkinter as tk
from tkinter import ttk
from chart_plotter import create_chart_frame
from tkinter import Listbox, Scrollbar, SINGLE

def update_chart_frame_selection(event, listbox, main_frame):
    selection_index = listbox.curselection()
    if not selection_index:
        return
    selection_pair = listbox.get(selection_index)

    #Fetch data for selected pair.
    new_data = fetch_crypto_data(selection_pair, period='5d', interval='1h')

    #update chart with new data.
    update_chart(main_frame, new_data)



def create_main_window(crypto_data, crypto_pairs):
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
    main_frame.pack(fill='both', expand=True)

    # Configure the weight of rows and columns
    main_frame.columnconfigure(0, weight=1)
    main_frame.columnconfigure(1, weight=1)
    main_frame.columnconfigure(2, weight=1)
    main_frame.columnconfigure(3, weight=1)
    main_frame.rowconfigure(0, weight=4)
    main_frame.rowconfigure(1, weight=1)
    main_frame.rowconfigure(2, weight=1) 
    main_frame.rowconfigure(3, weight=1) 

    #Addin listbox to hold crypto pairs.
    listbox_frame = ttk.Frame(main_frame)
    listbox_frame.grid(row=0, column=4, rowspan=4, sticky='nsew', padx=(5, 0))
    main_frame.columnconfigure(4, weight=1)

    scrollbar = Scrollbar(listbox_frame, orient="vertical")
    listbox = Listbox(listbox_frame, yscrollcommand=Scrollbar.set,
                      selectmode=SINGLE)
    scrollbar.config(command=listbox.yview)
    scrollbar.pack(side="right", fill="y")
    listbox.pack(side="left", fill="both", expand=True)

    #populate listbox with crypto pairs.
    for pair in crypto_pairs:
        listbox.insert(tk.END, pair)
    
    #Binding selected event to the listbox.
    listbox.bind('<<ListboxSelect>>', lambda event: update_chart_frame_selection(event, listbox,
                                                                                 chart_frame))

    #Chart Area.
    chart_frame = ttk.Frame(main_frame, borderwidth=2, relief="sunken")
    chart_frame.grid(row=0, column=1, columnspan=2, pady=5, padx=5, sticky="nsew")

    create_chart_frame(chart_frame, crypto_data)

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