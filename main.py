from tkinter import *


def miles_to_km():
    try:
        miles = float(entry.get())
        result = round(miles * 1.609, 2)
        label_result.config(text=f"{result}")
    except ValueError:
        label_result.config(text="Invalid")


window = Tk()
window.title("Mile to KM converter.")
window.config(padx=20, pady=20)

# Entry

entry = Entry(width=7)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

# Label

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to")
label_equal.grid(column=0, row=1)

label_result = Label(text="0")
label_result.grid(column=1, row=1)

label_km = Label(text="KM")
label_km.grid(column=2, row=1)

# Button

button = Button(text="Convert", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
