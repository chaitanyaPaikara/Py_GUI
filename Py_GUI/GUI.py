from Tkinter import *

root = Tk()

One = Label(root, text="One", bg="red", fg="green")
Two = Label(root, text="Two", bg="white", fg="blue")
Three = Label(root, text="Three", bg="yellow", fg="purple")

One.pack()
Two.pack(fill=X)
Three.pack(side=LEFT, fill=Y)

root.mainloop()
