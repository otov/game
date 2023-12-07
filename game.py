from tkinter import*
from tkinter import messagebox
gamewindow=Tk()
gamewindow.title("TicTacToe")


playerx=True
count=0


def btnclick(button):
    global playerx,count
    if button["text"]==" "and playerx==True:
        button["text"]="X"
        playerx=False
        count+=1
        checkwinner()
    elif button["text"]==" "and playerx==False:
        button["text"]="O"
        playerx=True
        count+=1
        checkwinner()
    else:
        messagebox.showerror("TicTacToe","This button is already presed!")
    return 


btn1=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn1),bg="#32CD32",activebackground="#32CD32",bd=5)
btn2=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn2),bg="#FF6103",activebackground="#FF6103",bd=5)
btn3=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn3),bg="#32CD32",activebackground="#32CD32",bd=5)
btn4=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn4),bg="#FF6103",activebackground="#FF6103",bd=5)
btn5=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn5),bg="#32CD32",activebackground="#32CD32",bd=5)
btn6=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn6),bg="#FF6103",activebackground="#FF6103",bd=5)
btn7=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn7),bg="#32CD32",activebackground="#32CD32",bd=5)
btn8=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn8),bg="#FF6103",activebackground="#FF6103",bd=5)
btn9=Button(gamewindow,text=" ",width=6,height=3,font=("Helvica",24),command=lambda:btnclick(btn9),bg="#32CD32",activebackground="#32CD32",bd=5)


def checkwinner():
    global winner
    winner=False
    if (btn1["text"]=="X"and btn2["text"]=="X" and btn3["text"]=="X" or btn4["text"]=="X"and btn5["text"]=="X" and btn6["text"]=="X" or btn7["text"]=="X"and btn8["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X"and btn4["text"]=="X" and btn7["text"]=="X" or btn2["text"]=="X"and btn5["text"]=="X" and btn8["text"]=="X" or btn3["text"]=="X"and btn6["text"]=="X" and btn9["text"]=="X" or btn1["text"]=="X"and btn5["text"]=="X" and btn9["text"]=="X" or btn3["text"]=="X"and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        messagebox.showinfo("TicTacToe", "Player X wins!")
        disablebutton()
    elif (btn1["text"]=="O"and btn2["text"]=="O" and btn3["text"]=="O" or btn4["text"]=="O"and btn5["text"]=="O" and btn6["text"]=="O" or btn7["text"]=="O"and btn8["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O"and btn4["text"]=="O" and btn7["text"]=="O" or btn2["text"]=="O"and btn5["text"]=="O" and btn8["text"]=="O" or btn3["text"]=="O"and btn6["text"]=="O" and btn9["text"]=="O" or btn1["text"]=="O"and btn5["text"]=="O" and btn9["text"]=="O" or btn3["text"]=="O"and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        messagebox.showinfo("TicTacToe", "Player O wins!")
        disablebutton()
    elif count==9 and winner==False:
        messagebox.showinfo("TicTacToe","Draw!")
        disablebutton()
    return


def disablebutton():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)
    return 0


def reset():
    global count, playerx
    count=0
    playerx=True
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    

    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "
    return


def gamerules():
    Newwindow=Toplevel()
    Newwindow.title("Game rules")
    Newwindow.geometry("520x100")
    Rules=Label(Newwindow,text="One player uses the symbol X. The other player uses O. ")
    Rules.grid(row=1,column=0)
    Rules=Label(Newwindow,text="The players take turns placing one symbol in one square. A square can contain only one symbol!")
    Rules.grid(row=2,column=0)
    Rules=Label(Newwindow,text="First player that places three of their symbols in a row (Horizontaly, vertically, diagonaly) wins!")
    Rules.grid(row=3,column=0)
    return 0


Mainmenu=Menu(gamewindow)
gamewindow.config(menu=Mainmenu)


options=Menu(Mainmenu,tearoff=False)
Mainmenu.add_cascade(label="Options",menu=options)


options.add_command(label="New game",command=reset)
options.add_command(label="Exit game",command=gamewindow.quit)

Mainmenu.add_command(label="Game rules",command=gamerules)


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