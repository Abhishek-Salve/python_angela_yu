# import tkinter
from tkinter import *


# buttons event listener
def button_clicked():
    print("Button clicked")
    # Method 1
    label["text"] = input.get()

    # Method 2
    # new_text = input.get()
    # label.config(text=new_text)


# below command is similar to turtle screen
window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=400)


# Label
label = Label(text="This is a label", font=("Arial", 14))   # font=(name of font, size of font, bold/italic)
label.grid(column=0, row=0)

# Button
button_1 = Button(text="button 1", command=button_clicked)
button_1.grid(column=1, row=1)

# Button
button_2 = Button(text="button 2", command=button_clicked)
button_2.grid(column=2, row=0)


# Entry --> text input entry box
input = Entry(width=40)
print(input.get())
input.grid(column=3, row=2)



# command to make the GUI wait
window.mainloop()
