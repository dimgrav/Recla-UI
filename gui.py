from tkinter import Button, Entry, Label, Tk

# window setup
window = Tk()
window.geometry('300x135')
window.resizable(0, 0)
window.title('Recla UI')

# lat/lon input
Label(window, text='Latitude').grid(row=0, sticky='W')
Entry(window).grid(row=0, column=1)
Label(window, text='Longitude').grid(row=1, sticky='W')
Entry(window).grid(row=1, column=1)

# color temp input
Label(window, text='DT Temperature').grid(row=2, sticky='W')
Entry(window).grid(row=2, column=1)
Label(window, text='NT Temperature').grid(row=3, sticky='W')
Entry(window).grid(row=3, column=1)

# close on click
Button(window, text='OK', command=lambda: window.destroy()).grid(columnspan=2, pady=5)

window.mainloop()
