# import tkinter
from tkinter import *


# buttons event listener
def button_clicked():
    print("Button clicked")
    label["text"] = input.get()


# below command is similar to turtle screen
window = Tk()
window.title("First GUI program")
window.minsize(width=500, height=400)


# Label
# font=(name of font, size of font, bold/italic)
label = Label(text="This is a label", font=("Arial", 14))
# how will this label be lay-ed out - important to display the label
# label.pack(side="left")
label.pack()

# Change the label - my just reassigning value to a dict key
# label["text"] = "Hello"


# Button
button = Button(text="button 1", command=button_clicked)
button.pack()


# Entry --> text input entry box
input = Entry(width=40)
# Add some text to begin with - this is not background watermark text, but actual text
input.insert(END, string="some text : ")
# Gets text in entry
print(input.get())
input.pack()


# Textbox
text = Text(height=3, width=40)  # set number of lines as height of box
# puts cursor in textbox
text.focus()
# add some initial text
text.insert(END, "example text")
# gets current value in textbox at line1, character 01
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets current value in spinbox
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=7, width=40, command=spinbox_used)
spinbox.pack()


# Scale
# called with current value of scale
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbox
def checkbutton_used():
    # print 1 if button is "checked"
    print(checked_state.get())

checked_state = IntVar()  # IntVar() is a class
checkbutton = Checkbutton(text="Working ?", variable = checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radio button - only one can be selected at one time
def radio_used():
    print(radio_state.get())

# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()



# command to make the GUI wait
window.mainloop()
