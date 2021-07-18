from tkinter import*
#Create a GUI window
window=Tk()
def from_kg():
    #Convert kg to gram
    gram=float(e2_value.get())*1000
    #Convert kg to pound
    pound=float(e2_value.get())*2.20462
    #Convert kg to ounce
    ounce=float(e2_value.get())*35.274
    #Enter the converted weight to the text widget

    t1.delete("1.0",END)
    t1.insert(END,gram)

    t2.delete("1.0",END)
    t2.insert(END,pound)

    t3.delete("1.0",END)
    t3.insert(END,ounce)
#Create the lable widgets
e1=Label(window,text="Enter the weight in kg" )
e2_value=StringVar()
e2=Entry(window,textvariable=e2_value)
e3=Label(window,text='Gram')
e4=Label(window,text='Pounds')
e5=Label(window,text='Ounce')
#Craete the text widgets
t1=Text(window , height=2, width=25)
t2=Text(window , height=2, width=25)
t3=Text(window , height=2, width=25)
#Craete Button widget
b1=Button(window,text="convert",command=from_kg)

e1.grid(row=0,column=0)
e2.grid(row=0,column=1)
e3.grid(row=1,column=0)
e4.grid(row=1,column=1)
e5.grid(row=1,column=2)
t1.grid(row=2,column=0)
t2.grid(row=2,column=1)
t3.grid(row=2,column=2)
b1.grid(row=0,column=2)

window.mainloop()