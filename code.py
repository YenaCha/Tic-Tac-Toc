from faulthandler import disable
from tkinter import *
import tkinter.messagebox
tk = Tk()
tk.title('Tic Tac Toc')
player1 = StringVar()
player2 = StringVar()
player1_box = Entry(tk, textvariable=player1, bd=5)
player2_box = Entry(tk, textvariable=player2, bd=5)
player1_box.grid(row=1, column=1)
player2_box.grid(row=2, column=1)
player1_label = Label(tk, text='Player 1', font='Times 20 bold',
                      bg='white', fg='black', height=1, width=8)
player2_label = Label(tk, text='Player 2', font='Times 20 bold',
                      bg='white', fg='black', height=1, width=8)
player1_label.grid(row=1, column=0)
player2_label.grid(row=2, column=0)

bclick = True
flag = 0
def buttonvalue(b):
    global bclick,flag
    if(bclick == True and b['text']==' '):
        b['text'] = 'X'
        bclick = False
        flag = flag+1
        checkwinning()
    elif(bclick == False and b['text']==' '):
        b['text'] = 'O'
        bclick = True
        flag = flag+1
        checkwinning()

def disablebuttons():
    button1.configure(state= DISABLED)
    button2.configure(state= DISABLED)
    button3.configure(state= DISABLED)
    button4.configure(state= DISABLED)
    button5.configure(state= DISABLED)
    button6.configure(state= DISABLED)
    button7.configure(state= DISABLED)
    button8.configure(state= DISABLED)
    button9.configure(state= DISABLED)

def checkwinning():
    if(button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
       button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
       button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
       button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
       button3['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X' or
       button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
       button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X'):
        disablebuttons()
        tkinter.messagebox.showinfo('Tic Tac Toc',player1.get()+' wins')
    elif(button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
       button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
       button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
       button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
       button3['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O' or
       button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
       button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O'):
        disablebuttons()
        tkinter.messagebox.showinfo('Tic Tac Toc',player2.get()+' wins')


button1 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button1))
button1.grid(row=3, column=0)
button2 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button2))
button2.grid(row=3, column=1)
button3 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button3))
button3.grid(row=3, column=2)
button4 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button4))
button4.grid(row=4, column=0)
button5 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button5))
button5.grid(row=4, column=1)
button6 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button6))
button6.grid(row=4, column=2)
button7 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button7))
button7.grid(row=5, column=0)
button8 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button8))
button8.grid(row=5, column=1)
button9 = Button(tk, text=' ', font='Times 20 bold',
                 bg='gray', fg='white', width=8, height=4, command=lambda:buttonvalue(button9))
button9.grid(row=5, column=2)

tk.mainloop()
