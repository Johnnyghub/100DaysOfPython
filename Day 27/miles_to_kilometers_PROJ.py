from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=200)

label = Label(text="is equal to")
label.grid(column=0, row=1)

miles_input = Entry()
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

km = Label(text="0")
km.grid(column=1, row=1)


def calculate_km():
    miles = miles_input.get()
    kilometers = round((float(miles) * 1.609), 2)
    km.config(text=f"{kilometers}")


button = Button(text="Click Me", command=calculate_km)
button.grid(column=1, row=2)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

window.mainloop()
