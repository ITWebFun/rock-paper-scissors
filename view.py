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

#we made a label widget to add the label that informs the user about entering his/her name in rock, paper and sicssor game
name=Label(root,text='Enter Your Name :',font='arial 15 bold')
name.place(x=262,y=250)

#This below variable will store the name of user and will further be used to display the name of the user wherever we want to display
nameinp=StringVar()
inpname=Entry(root,textvar=nameinp,font='arial 10 bold')
#We binded Return event with inpname entry widget i.e. if enter key is pressed then entergame function will be called
inpname.bind('<Return>',controller.start_game)  
inpname.place(x=275,y=290)

#this is the button that will appear on the home username window
#a button of lets play is added so that the user can enter the main game window once the username is added
sub=Button(root,text="Let's Play",font='lucida 10 bold',bg='black',fg='white',command=controller.play)
sub.place(x=305,y=350)

root.mainloop()