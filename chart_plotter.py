import mplfinance as mpf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def create_chart_frame(parent, data, width, height):
    #Set style for the plot.
    mpf_style = mpf.make_mpf_style(base_mpf_style='charles',
                               rc={'font.size':8})

    #create figure for the plot
    fig, axes = mpf.plot(data, type='candle', style=mpf_style,
                     returnfig=True) 

    #Create canvas with figure in it.
    canvas = FigureCanvasTkAgg(fig, master=parent)
    canvas.draw()

    #Place canvas in tkinter window.
    chart_widget = canvas.get_tk_widget()
    chart_widget.configure(width=width, height=height)
    chart_widget.pack(side="top", fill="both", expand=True)

    return canvas