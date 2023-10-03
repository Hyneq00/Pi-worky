from tkinter import *


def try_name():
            global player1
            global player2
            global run
            player1 = input1.get()
            player2 = input2.get()
            window.destroy()
            

window = Tk()
window.title("Input name")
window.minsize(500, 500)
window.resizable(False, False)


    #vložení jmen
empty = Label(text="                                   ",font=("Ariel", 20))
empty.grid(row=0, column=0)
text = Label(text="Vložte jmena hráčů", font=("Ariel", 20))
text.grid(row=1, column=1)
empty2 = Label(text="                                   ",font=("Ariel", 20))
empty2.grid(row=2, column=0)  
name1 = Label(text="Player 1", font=("Ariel", 20))
name1.grid(row=3, column=1)
input1 = Entry(width=10,font= ("Ariel", 20))
input1.grid(row=4, column=1)
empty3 = Label(text="                                   ",font=("Ariel", 20))
empty3.grid(row=5, column=0)
name2 = Label(text="Player 2", font=("Ariel",20))
name2.grid(row=6, column=1)
input2 = Entry(width=10,font= ("Ariel", 20))
input2.grid(row=7, column=1)
button = Button(text="Začít hrát", font=("Ariel", 20), command=try_name)
button.grid(row=8, column=1)


    # Hlavní cyklus
window.mainloop()
