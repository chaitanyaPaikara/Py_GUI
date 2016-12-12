from Tkinter import *

root = Tk()
def leftclick(evenet):
    print("Mouse Left Click")
def middleclick(event):
    print("Mouse Middle Click")
def rightclick(event):
    print("Mouse Right Click")

frame = Frame(root, width=300, height=700)
frame.bind("<Button-1>",leftclick)
frame.bind("<Button-2>",middleclick)
frame.bind("<Button-3>",rightclick)
frame.pack()
root.mainloop()
