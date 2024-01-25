import mplfinance as mpf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

def create_chart_frame(parent, data):
    # Set style for the plot
    mpf_style = mpf.make_mpf_style(base_mpf_style='charles', rc={'font.size':8})

    # Create figure for the plot
    fig = Figure(figsize=(5, 4), dpi=100)  
    ax = fig.add_subplot(111)

    # Plot the data on the figure
    mpf.plot(data, ax=ax, type='candle', style=mpf_style)

    # Create the canvas and put the figure in it
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()

    # Configure the canvas to fill the frame
    canvas.get_tk_widget().pack(fill='both', expand=True)

    return canvas