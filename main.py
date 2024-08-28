from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

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


window.mainloop()