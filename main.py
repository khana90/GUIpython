from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=400)

# Label
my_labl =Label(text="I am a label", font=("Arial", 24))
my_labl.pack()
my_labl["text"] = "New Text"
my_labl.config(text= "new text")

# Button
def button_clicked():
  print("i got clicked")
  my_text=input.get()
  my_labl.config(text=my_text)


button=Button(text="click me",command=button_clicked)
button.pack()

# Entry
input = Entry(width=10)
input.pack()

# spinbox
def spinbox_used():
  print(spinbox.get())
spinbox=Spinbox(from_=0, to=10, width=9, command=spinbox_used)
spinbox.pack()

# scale
def scale_used(value):
  print(value)
scale=Scale(from_=0, to=100, command=scale_used)
scale.pack()

# entries
entry= Entry(width=30)

entry.insert(END, string="some text")
print(entry.get())
entry.pack()

# text
text=Text(height=5, width=30)
# put curser in textbox
text.focus()
# add some text to begin with
text.insert(END, "Example of multi-line text entry")
# get's current value in textbox at line 1, character
print(text.get("1.0", END))
text.pack()

window.mainloop()