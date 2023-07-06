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

#functions for the rock, paper & scissors buttons
def enter(event):
    event.widget.config(bg='black',fg='white')
def leave(event):
    event.widget.config(bg='white',fg='black')
def click(event):
    controller.play(event.widget.cget('text'))

#creating the game window        
def main_game_window():
    
    #the below are the set of buttons that are available for the player 1
    rock=Button(text='Rock',font='comicsansms 18 bold',height=1,width=7)
    rock.grid(row=3,column=0,pady=15)
    #the bind() is used to bind multiple methods in the Program
    rock.bind('<Enter>',enter)
    rock.bind('<Leave>',leave)
    rock.bind('<Button-1>',click)
    paper=Button(text='Paper',font='comicsansms 18 bold',height=1,width=7)
    paper.grid(row=4,column=0)
    paper.bind('<Enter>',enter)
    paper.bind('<Leave>',leave)
    paper.bind('<Button-1>',click)
    scissor=Button(text='Scissor',font='comicsansms 18 bold',height=1,width=7)
    scissor.grid(row=5,column=0,pady=15)
    scissor.bind('<Enter>',enter)
    scissor.bind('<Leave>',leave)
    scissor.bind('<Button-1>',click)

#enters the main game window
def start_game():
    controller.set_user_name(nameinp)
    frame.destroy()
    logo_label.destroy()
    name.destroy()
    inpname.destroy()
    sub.destroy()
    main_game_window()

#This below variable will store the name of user and will further be used to display the name of the user wherever we want to display
nameinp=StringVar()
inpname=Entry(root,textvar=nameinp,font='arial 10 bold')
#We binded Return event with inpname entry widget i.e. if enter key is pressed then entergame function will be called
inpname.bind('<Return>',start_game)  
inpname.place(x=275,y=290)

#this is the button that will appear on the home username window
#a button of lets play is added so that the user can enter the main game window once the username is added
sub=Button(root,text="Let's Play",font='lucida 10 bold',bg='black',fg='white',command=start_game)
sub.place(x=305,y=350)

root.mainloop()