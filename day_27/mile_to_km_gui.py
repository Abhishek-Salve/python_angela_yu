from tkinter import  *

from numpy.ma.core import count

window = Tk()
window.title("Mile to Km converter")
window.config(padx=20, pady=20)
# window.minsize(height=200, width = 300)


def convert_onclick():
    miles = float(km_entry.get())
    kms = miles * 1.609
    km_convert.config(text="{:.2f}".format(kms))


# Entry
km_entry = Entry(width=7)
print(km_entry.get())
km_entry.grid(column=1, row=0)

# Label 1
label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)
# label_1.config(padx=10, pady=0)

# Label 2
label_2 = Label(text=" miles")
label_2.grid(column=2, row=0)
# label_2.config(padx=5, pady=5)

# Label 3
label_3 = Label(text=" kms")
label_3.grid(column=2, row=1)
# label_3.config(padx=5, pady=5)

# Label 4
km_convert = Label(text=" ")
km_convert.grid(column=1, row=1)
# km_convert.config(padx=40, pady=20)

# Calculate button
calc_button = Button(text="Calculate", command=convert_onclick)
calc_button.grid(column=1, row=2)
# calc_button.config(padx=10, pady=0)


# Wait
window.mainloop()
