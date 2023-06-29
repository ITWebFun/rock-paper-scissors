from tkinter import *
from PIL import ImageTk, Image

root = Tk()

root.title('Rock, Paper, Scissors')
root.minsize(700,450)
root.maxsize(750,450)

game_name = Label(text='Rock, Paper, Scissors!',font='arial 35 bold',bg='black',fg='white')
game_name.grid(row=0,ipadx=70,padx=33,pady=10)

img=Image.open('symbols.png')
img=img.resize((650,450),Image.ANTIALIAS)
ic=ImageTk.PhotoImage(img)


root.mainloop()