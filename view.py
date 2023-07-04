from tkinter import *
from PIL import ImageTk, Image
import os, controller

print('path: ' + os.getcwd())

root = Tk()

root.title('Rock, Paper, Scissors')
root.minsize(725,450)
root.maxsize(725,450)

frame = Frame(root, width=400, height=150)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(os.getcwd() + '\images\symbols.png'))

# Create a Label Widget to display the text or Image
logo_label = Label(frame, image = img)
logo_label.grid(row=0,ipadx=70,padx=33,pady=10)

game_name = Label(text='Rock, Paper, Scissors!',font='arial 35 bold',bg='black',fg='white')
game_name.grid(row=1,ipadx=70,padx=33,pady=10)

play_btn = Button(text='Play',font='lucida 18 bold',command=controller.maingame)
play_btn.grid(row=2,ipadx=70,padx=33,pady=10)

root.mainloop()