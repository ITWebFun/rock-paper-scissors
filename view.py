from tkinter import *
from PIL import ImageTk, Image
import os, controller

cwd = os.getcwd()

root = Tk()

root.title('Rock, Paper, Scissors')
root.wm_iconbitmap(cwd + "\images\play.ico")
root.minsize(725,450)
root.maxsize(725,450)

frame = Frame(root, width=400, height=150)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open(cwd + '\images\symbols.png'))

# Create a Label Widget to display the text or Image
logo_label = Label(frame, image = img)
logo_label.grid(row=0,ipadx=70,padx=33,pady=10)

game_name = Label(text='Rock, Paper, Scissors!',font='arial 35 bold',bg='black',fg='white')
game_name.grid(row=1,column=0,columnspan=2,ipadx=70,padx=33,pady=10)

#we made a label widget to add the label that informs the user about entering his/her name in rock, paper and sicssor game
name=Label(root,text='Enter Your Name :',font='arial 15 bold')
name.place(x=262,y=250)

#functions for the rock, paper & scissors buttons
def enter(event):
    event.widget.config(bg='black',fg='white')
def leave(event):
    event.widget.config(bg='white',fg='black')

#creating the game window        
def main_game_window():
    
    def click(event):
        win_label.config(text = controller.play(event.widget.cget('text')),font='comicsansms 18 bold')
        player_score.config(text=f'{controller.user.get_name()} Score: {controller.user.get_score()}',font='comicsansms 18 bold')
        computer_score.config(text=f'Computer Score: {controller.computer.get_score()}',font='comicsansms 18 bold')
    
    #the below are the set of buttons that are available for the player 1
    rock=Button(text='Rock',font='comicsansms 18 bold',height=1,width=7)
    rock.grid(row=3,column=0,padx=0,pady=15)
    #the bind() is used to bind multiple methods in the Program
    rock.bind('<Enter>',enter)
    rock.bind('<Leave>',leave)
    rock.bind('<Button-1>',click)
    paper=Button(text='Paper',font='comicsansms 18 bold',height=1,width=7)
    paper.grid(row=4,column=0,padx=0, pady = 15)
    paper.bind('<Enter>',enter)
    paper.bind('<Leave>',leave)
    paper.bind('<Button-1>',click)
    scissors=Button(text='Scissors',font='comicsansms 18 bold',height=1,width=7)
    scissors.grid(row=5,column=0,padx=0,pady=15)
    scissors.bind('<Enter>',enter)
    scissors.bind('<Leave>',leave)
    scissors.bind('<Button-1>',click)
    
    #info labels with player and computer score and the pick of the computer
    player_score = Label(text=f'{controller.user.get_name()} Score: {controller.user.get_score()}',font='comicsansms 18 bold')
    player_score.grid(row=3, column=1)
    computer_score = Label(text=f'Computer Score: {controller.computer.get_score()}',font='comicsansms 18 bold')
    computer_score.grid(row=4, column=1)
    win_label = Label(text='',font='comicsansms 18 bold')
    win_label.grid(row=5, column=1)
    
    end_btn = Button(text='End game!',font='comicsansms 18 bold',height=1,width=7,command=root.destroy)
    end_btn.grid(row=6, column=0, columnspan=2, ipadx=15)
    end_btn.bind('<Enter>',enter)
    end_btn.bind('<Leave>',leave)

#enters the main game window
def start_game(event=None):
    controller.set_user_name(input_name.get())
    frame.destroy()
    logo_label.destroy()
    name.destroy()
    input_name.destroy()
    sub.destroy()
    main_game_window()
    

#This below variable will store the name of user and will further be used to display the name of the user wherever we want to display
#nameinp=StringVar()
#input_name=Entry(root,textvar=nameinp,font='arial 10 bold')
input_name=Entry(root,font='arial 10 bold')
#We binded Return event with input_name entry widget i.e. if enter key is pressed then entergame function will be called
input_name.bind('<Return>',start_game)  
input_name.place(x=275,y=290)

#this is the button that will appear on the home username window
#a button of lets play is added so that the user can enter the main game window once the username is added
sub=Button(root,text="Let's Play",font='lucida 10 bold',bg='black',fg='white',command=start_game)
sub.place(x=305,y=350)

root.mainloop()