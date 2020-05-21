import math
from  tkinter import *


def leftClickButton(event):
    Number = float(textBoxWeight.get())/math.pow(float(textBoxHeight.get())/100,2)
    print(Number)
    labelResultNumber.configure(text=Number)
    if Number >= 30 :
        labelResult.configure(text="อ้วนมาก")
    elif Number >=25 :
        labelResult.configure(text="อ้วน")
    elif Number >=23 :
        labelResult.configure(text="น้ำหนักเกิน")
    elif Number >=18.6:
        labelResult.configure(text="เหมาะสม")
    else:
        labelResult.configure(text="ผอมเกินไป")

MainWindow = Tk()
labelHeight = Label(MainWindow,text="ส่วนสูง (cm.)").grid(row=0, column=0)
textBoxHeight = Entry(MainWindow)
textBoxHeight.grid(row=0, column=1)
labelWeight = Label(MainWindow,text="น้ำหนัก (Kg.)").grid(row=1, column=0)
textBoxWeight = Entry(MainWindow)
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(MainWindow,text = "คำนวณ")
calculateButton.grid(row=2)
calculateButton.bind('<Button-1>',leftClickButton)
labelResultNumber = Label(MainWindow,text="ผลลัพธ์")
labelResultNumber.grid(row=2, column=1)
labelResult = Label(MainWindow,text="สรุป")
labelResult.grid(row=2,column=2)
MainWindow.mainloop()
