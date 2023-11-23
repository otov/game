from tkinter import*
from tkinter import messagebox
gamewindow=Tk()
gamewindow.title("TicTacToe")


playerx=True
count=0


btn1=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn2=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn3=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn4=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn5=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn6=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn7=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn8=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))
btn9=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24))


def btnclick(button):
    global playerx,count
    if button["text"]==""and playerx==True:
        button["text"]="X"
        playerx=False
        count+=1
    elif button["text"]==""and playerx==False:
        button["text"]="O"
        playerx=True
        count+=1
    else:
        messagebox.showerror("TicTacToe","!")


command=lambda:btnclick(btn1)
command=lambda:btnclick(btn2)
command=lambda:btnclick(btn3)
command=lambda:btnclick(btn4)
command=lambda:btnclick(btn5)
command=lambda:btnclick(btn6)
command=lambda:btnclick(btn7)
command=lambda:btnclick(btn8)
command=lambda:btnclick(btn9)


def checkwinner():
    global winner
    winner=False
    if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" or btn4["text"]=="X"and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"]=="X"and btn8["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X" or btn3["text"]=="X"and btn6["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X" or btn3["text"]=="X"and btn6["text"]=="X" and btn7["text"]=="X"):
        winner=True
        messagebox.showinfo("TicTacToe", "Player X wins!")
    elif (btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O" or btn4["text"]=="O"and btn5["text"]=="O" and btn6["text"]=="O" or btn7["text"]=="O"and btn8["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O"and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"]=="O"and btn5["text"]=="O" and btn8["text"]=="O" or btn3["text"]=="O"and btn6["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O"and btn5["text"]=="O" and btn9["text"]=="O" or btn3["text"]=="O"and btn6["text"]=="O" and btn7["text"]=="O"):
        winner=True
        messagebox.showinfo("TicTacToe", "Player O wins!")
    elif count==9 and winner==False:
        messagebox.showinfo("TicTacToe","Draw!")



btn1.grid(row=0,column=0)
btn2.grid(row=0,column=1)
btn3.grid(row=0,column=2)
btn4.grid(row=1,column=0)
btn5.grid(row=1,column=1)
btn6.grid(row=1,column=2)
btn7.grid(row=2,column=0)
btn8.grid(row=2,column=1)
btn9.grid(row=2,column=2)



gamewindow.mainloop()