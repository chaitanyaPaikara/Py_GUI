from Tkinter import *
window = Tk()
window.configure(width=320,height=240,background="#f4f3f1",bd=20,highlightbackground="green", highlightcolor="turquoise4", highlightthickness=5)#"#a1dbcd"  "#202d4e"
window.title("Segre-G-A-TOR")
def Click():
    global last, theLabel
    theLabel.pack_forget()
    string = ent.get()
    if string=='Metal':
        present = w_metal
    elif string=='Organic':
        present = w_organic
    elif string=='Plastic':
        present = w_plastic
    #present.grid(row=0, column=0)
    present.pack(side = LEFT)
    last.pack_forget() #last.grid_forget()
    last = present

    theLabel = Label(window, text=string, font=("Helvetica", 50), fg="#11dbcd", bg="#f4f3f1")
      # theLabel.grid_forget()
    theLabel.pack(side = RIGHT)#theLabel.grid(row=0, column=1)
    '''
    else:
        theLabel = Label(window, text="SHIT!!!", font=("Comic sans", 16), fg="#11dbcd", bg="#202d4e")
        theLabel.grid(row=0,column=0)
    '''
btn = Button(window,text="Accept",fg="#11dbcd", bg="#383a39",command=Click)
global ent, w_metal, w_organic, w_plastic, theLabel, last
img = PhotoImage(file="resize_Best.gif",width=320,height=88)
theLabel = Label(window, image=img, width=320, height=88)
theLabel.pack(fill=X)
last = Label(window, text="ADD WASTE", font=("Comic sans", 16), fg="#11dbcd", bg="#f4f3f1")
last.pack()
img_metal = PhotoImage(file="metal.gif")
img_orgaic = PhotoImage(file="organic.gif")
img_plastic = PhotoImage(file="plastic.gif")
w_metal = Label(window, image=img_metal)
w_organic = Label(window, image=img_orgaic)
w_plastic = Label(window, image=img_plastic)
ent = Entry(window)
btn.pack(side = BOTTOM)
ent.pack(side = BOTTOM)

window.geometry('320x240')
window.mainloop()