from tkinter import*

def click(event):          # Fuction for button to perform caluation
    global scvalue
    text = event.widget.cget("text")  # Geting text value from screen 
    # print(text)     # print text value on the console
    if text=="=":    # if user click the "=" Butoon 
        if scvalue.get().isdigit():  # Validating the input values are only digit or not 
            value = int(scvalue.get())  # If there is only digit then conver in integer
        else:
            try:
                value = eval(screen.get())  # If there is operand with digit then perform calculation
            except Exception as e:
                scvalue.set("Error")  # If there is invalid input then print erroe message on the screen
                screen.update()
        scvalue.set(value)
        screen.update()
    elif text=="c":   # If user input is c then clear the screen 
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()   # Here creating object of tkinter class as  root
root.geometry("350x570") # Define the window size
root.title("Calculator")  # It is titile of the application
root.wm_iconbitmap("")  # It is icon of application

scvalue = StringVar()   # Creating tkinter class variable for geting value from calculator screen
scvalue.set("")   # set the screen null
#--------------------Creating Calculator Screen By using Entery class----------------------------
screen = Entry(root,textvar=scvalue,font="lucida 25 bold",relief=SUNKEN)
screen.pack(fill=X,ipady=8,ipadx=8,pady=7,padx=10)
#-----------------Creating first frame for number button "9 8 7"--------------------
f = Frame(root,bg="grey") # Creating frame
b = Button(f,text="9",font="lucida 20 bold",padx=20,relief=SUNKEN) # Creating button
b.pack(side=LEFT,padx=10,pady=5) # Packing the button
b.bind("<Button-1>",click)  # Binding the button with click function
b = Button(f,text="8",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="7",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack() # Packing the frame

#-----------------Creating 2nd first frame for number button "6 5 4"--------------------
f = Frame(root,bg="grey")
b = Button(f,text="6",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="5",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="4",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

#-----------------Creating 3nd frame for number button "3 2 1"--------------------
f = Frame(root,bg="grey")
b = Button(f,text="3",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="2",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="1",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

#-----------------Creating 4th frame for number button "0 - +"--------------------
f = Frame(root,bg="grey")
b = Button(f,text="0",font="lucida 20 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="-",font="lucida 22 bold",padx=20,relief=SUNKEN,bg="blue",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="+",font="lucida 20 bold",padx=20,relief=SUNKEN,bg="blue",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

#-----------------Creating 6th frame for number operators button--------------------
f = Frame(root,bg="grey")
b = Button(f,text="*",font="lucida 20 bold",padx=20,relief=SUNKEN,bg="blue",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="/",font="lucida 20 bold",padx=25,relief=SUNKEN,bg="blue",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="%",font="lucida 18 bold",padx=20,relief=SUNKEN,bg="blue",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root,bg="grey")
b = Button(f,text="=",font="lucida 20 bold",padx=20,relief=SUNKEN,bg="green",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text="c",font="lucida 20 bold",padx=20,relief=SUNKEN,bg="red",fg="white")
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
b = Button(f,text=".",font="lucida 24 bold",padx=20,relief=SUNKEN)
b.pack(side=LEFT,padx=10,pady=5)
b.bind("<Button-1>",click)
f.pack()



root.mainloop()