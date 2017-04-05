from Tkinter import *

root = Tk()
def leftclick(evenet):
    global theLabel
    theLabel = Label(root, text="Hello How are you",font=("Helvetica", 16), fg="SlateBlue4", bg="DarkOrchid4")
    theLabel.grid(row=0, column=0)
    print("Mouse Left Click")
def middleclick(event):
    print("Mouse Middle Click")
def rightclick(event):
    #theLabel.config(font=("Courier", 44))
    theLabel.grid_forget()
    print("Mouse Right Click")

frame = Frame(root, width=320, height=240, bg="DarkOrchid4")
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",middleclick)
frame.bind("<Button-3>",rightclick)
frame.grid(row=0,column=0)
root.mainloop()
