from tkinter import *
from tkinter import Button
from tkinter import messagebox

val = ""
A = 0
operator = ""


def btn1_clicked():
    global val
    val = val + "1"
    data.set(val)


def btn2_clicked():
    global val
    val = val + "2"
    data.set(val)


def btn3_clicked():
    global val
    val = val + "3"
    data.set(val)


def btn4_clicked():
    global val
    val = val + "4"
    data.set(val)


def btn5_clicked():
    global val
    val = val + "5"
    data.set(val)


def btn6_clicked():
    global val
    val = val + "6"
    data.set(val)


def btn7_clicked():
    global val
    val = val + "7"
    data.set(val)


def btn8_clicked():
    global val
    val = val + "8"
    data.set(val)


def btn9_clicked():
    global val
    val = val + "9"
    data.set(val)


def btn0_clicked():
    global val
    val = val + "0"
    data.set(val)


def btn_add_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "+"
    val = val + " +"
    data.set(val)


def btn_sub_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn_mul_clicked():
    global val
    global A
    global operator
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)


def btn_div_clicked():
    global val
    global A
    global operator
    A = float(val)
    operator = "/"
    val = val + "/"
    data.set(val)


def btn_equal_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "="
    val = val + "="
    data.set(val)


def c_clicked():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)


def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = float((val2.split("/")[1]))
        if x == 0:
            messagebox.show("Error", "Division by 0 Not Allowed")
            A == ""
            val = ""
            data.set(val)
        else:
            c = float(A / x)
            data.set(c)
            val = str(c)


window = Tk()
window.geometry("250x400+300+300")
window.title('Calculator')

data = StringVar()
label = Label(window, text='Label', anchor=SE, bg='#ffffff', font='sans 16 bold', fg='#000000', textvariable=data)
label.pack(expand=True, fill="both")

btn_row1 = Frame(window, bg='black')
btn_row1.pack(expand=True, fill="both")

btn_row2 = Frame(window)
btn_row2.pack(expand=True, fill="both")

btn_row3 = Frame(window)
btn_row3.pack(expand=True, fill="both")

btn_row4 = Frame(window)
btn_row4.pack(expand=True, fill="both")

btn1 = Button(btn_row1, text="1", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn1_clicked)
btn1.pack(side=LEFT, expand=True, fill='both')

btn2 = Button(btn_row1, text="2", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn2_clicked)
btn2.pack(side=LEFT, expand=True, fill='both')

btn3 = Button(btn_row1, text="3", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn3_clicked)
btn3.pack(side=LEFT, expand=True, fill='both')

btn4 = Button(btn_row1, text="+", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1',
              command=btn_add_clicked)
btn4.pack(side=LEFT, expand=True, fill='both')

btn1 = Button(btn_row2, text="4", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn4_clicked)
btn1.pack(side=LEFT, expand=True, fill='both')

btn2 = Button(btn_row2, text="5", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn5_clicked)
btn2.pack(side=LEFT, expand=True, fill='both')

btn3 = Button(btn_row2, text="6", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn6_clicked)
btn3.pack(side=LEFT, expand=True, fill='both')

btn4 = Button(btn_row2, text="-", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1',
              command=btn_sub_clicked)
btn4.pack(side=LEFT, expand=True, fill='both')

btn1 = Button(btn_row3, text="7", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn7_clicked)
btn1.pack(side=LEFT, expand=True, fill='both')

btn2 = Button(btn_row3, text="8", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn8_clicked)
btn2.pack(side=LEFT, expand=True, fill='both')

btn3 = Button(btn_row3, text="9", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn9_clicked)
btn3.pack(side=LEFT, expand=True, fill='both')

btn4 = Button(btn_row3, text="*", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1',
              command=btn_mul_clicked)
btn4.pack(side=LEFT, expand=True, fill='both')

btn1 = Button(btn_row4, text="c", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=c_clicked)
btn1.pack(side=LEFT, expand=True, fill='both')

btn2 = Button(btn_row4, text="0", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1', command=btn0_clicked)
btn2.pack(side=LEFT, expand=True, fill='both')

btn3 = Button(btn_row4, text="=", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1',
              command=result)
btn3.pack(side=LEFT, expand=True, fill='both')

btn4 = Button(btn_row4, text="/", font='sans 16 bold', relief=GROOVE, bg='#2e4053', fg='#ecf0f1',
              command=btn_div_clicked)
btn4.pack(side=LEFT, expand=True, fill='both')

window.mainloop()
