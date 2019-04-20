import os
from subprocess import call
from tkinter import Button, Entry, Label, Tk, StringVar

__author__ = "Dimitris Gravanis"
__copyright__ = "2019"
__version__ = "0.0.1"
__description__ = "Recla-UI: minimal GUI for Recla"
__abs_dirpath__ = os.path.dirname(os.path.abspath(__file__))


def run():
    """
    Start recla.py and close GUI window

    :return: nothing
    """

    window.destroy()
    call([
        'python3', f'{__abs_dirpath__}/recla.py',
        '-z', f'{lat.get()}',
        '-y', f'{lon.get()}',
        '-d', f'{dt_temp.get()}',
        '-n', f'{nt_temp.get()}'
    ])


# window setup
window = Tk()
window.geometry('300x135')
window.resizable(0, 0)
window.title('Recla UI')

lat, lon = StringVar(), StringVar()
dt_temp, nt_temp = StringVar(), StringVar()

# lat/lon input
Label(window, text='Latitude').grid(row=0, sticky='W')
lat_entry = Entry(window, textvariable=lat).grid(row=0, column=1)
Label(window, text='Longitude').grid(row=1, sticky='W')
lon_entry = Entry(window, textvariable=lon).grid(row=1, column=1)

# color temp input
Label(window, text='DT Temperature').grid(row=2, sticky='W')
dt_temp_entry = Entry(window, textvariable=dt_temp).grid(row=2, column=1)
Label(window, text='NT Temperature').grid(row=3, sticky='W')
nt_temp_entry = Entry(window, textvariable=nt_temp).grid(row=3, column=1)

# run Recla and close window on click
button = Button(window, text='OK', command=run).grid(columnspan=2, pady=5)

window.mainloop()
