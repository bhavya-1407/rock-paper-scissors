import emoji

from tkinter import *
from PIL import Image, ImageTk
from random import randint

window = Tk()
window.title("Rock Paper Scissors")
window.configure(background="#F8C8DC")

image_rock1 = ImageTk.PhotoImage(Image.open("rps_3_same_size(opp).png"))
image_paper1 = ImageTk.PhotoImage(Image.open("rps_1_same_size(opp).png"))
image_scissor1 = ImageTk.PhotoImage(Image.open("rps_2_same_size(opp).png"))

image_rock2 = ImageTk.PhotoImage(Image.open("rps_3_same_size.png"))
image_paper2 = ImageTk.PhotoImage(Image.open("rps_1_same_size.png"))
image_scissor2 = ImageTk.PhotoImage(Image.open("rps_2_same_size.png"))

# Left section - computer side
left_frame = Frame(window, bg="#F8C8DC")
left_frame.grid(row=0,column=0)
label_computer = Label(left_frame, image=image_scissor1)
label_computer.grid(row=0,column=0)
computer_indicator = Label(left_frame, font=("arial", 30, "bold"), text=emoji.emojize(":desktop_computer:"),bg="#F8C8DC", fg="#BCD8EC")

computer_indicator.grid(row=1, column=0)
# Centre - scores & buttons
centre_frame = Frame(window, bg="#F8C8DC")
centre_frame.grid(row=0, column=1)

#-> scores
score_frame = Frame(centre_frame, bg="#F8C8DC")
score_frame.grid(row=0,column=0)

computer_score = Label(score_frame, text=0, font=('arial', 60, "bold"),fg="#C096EA",bg="#F8C8DC")
computer_score.grid(row=0,column=1,padx=120)

player_score = Label(score_frame,text=0, font=('arial', 60, "bold"), fg="#C096EA",bg="#F8C8DC")
player_score.grid(row=0,column=4,padx=80)

#-> buttons
button_frame = Frame(window, bg="#F8C8DC")
button_frame.grid(row=2, column=1)

button_rock = Button(button_frame, width=7, height=2, text=emoji.emojize(":rock:"), font=("Arial", 30), bg="#FCF4A3",command=lambda:choice_update("rock")).grid(row=0,column=0,padx=5)
button_paper = Button(button_frame, width=7, height=2, text=emoji.emojize(":page_facing_up:"), font=("Arial", 30), bg="#FCF4A3",command=lambda:choice_update("paper")).grid(row=0, column=1,padx=5)
button_scissor = Button (button_frame, width=7, height=2, text=emoji.emojize(":scissors:"), font=("Arial",30), bg ="#FCF4A3",command=lambda:choice_update("scissor")).grid(row=0,column=2,padx=5)

#Right section - user side
right_frame = Frame(window, bg="#F8C8DC")
right_frame.grid(row=0,column=2)

player_indicator = Label(right_frame, font=("arial", 30, "bold"), text=emoji.emojize(":bust_in_silhouette:"),bg="#F8C8DC", fg="#BCD8EC")

player_indicator.grid(row=1,column=0)

label_player = Label(right_frame, image=image_scissor2)
label_player.grid(row=0,column=0)

final_message = Label(button_frame, font=("arial", 20, "bold"), bg="#F8C8DC", text="Choose your move!", fg="#BCD8EC")
final_message.grid(row=1,column=0, columnspan=3, pady=10)

def msg_updation(a):
    final_message['text'] = a

def computer_update():
    final = int(computer_score['text'])
    final += 1    
    computer_score["text"] = str(final)
    
def player_update():
    final = int(player_score['text'])
    final += 1    
    player_score["text"] = str(final)

def winner_check(p, c):
    if p == c:
        msg_updation("lwk twinning")
    elif p == "rock":
        if c == "paper":
            msg_updation("did you lose to a computer...in rock, paper, scissors?")
            computer_update()
        else:
            msg_updation("congratulations! you clearly have no friends <3")
            player_update()
    elif p == "paper":
        if c == "scissor":
            msg_updation("wow...")
            computer_update()
        else:
            msg_updation("at least you won here... ig")
            player_update()
    elif p == "scissor":
        if c == "rock":
            msg_updation("L. major L.")
            computer_update()
        else:
            msg_updation("yay.. you won your self-respect!")
            player_update()
    else:
        pass
            
to_select = ["rock", "paper", "scissor"]  

def make_choice(a):
    computer_score.config(text=old_c_score)
    player_score.config(text=old_p_score)
    
    choice_computer = to_select[randint(0,2)]
    
    if choice_computer == "rock":
        label_computer.configure(image=image_rock1)
    elif choice_computer == "paper":
        label_computer.configure(image=image_paper1)
    else:
        label_computer.configure(image=image_scissor1)
        
    if a == "rock":
        label_player.configure(image=image_rock2)
    elif a == "paper":
        label_player.configure(image=image_paper2)
    else:
        label_player.configure(image=image_scissor2)
        
    winner_check(a, choice_computer)

def choice_update(a):
    global old_c_score, old_p_score
    
    old_c_score = computer_score["text"]
    old_p_score = player_score["text"]
    
    computer_score.config(text="⏳")
    player_score.config(text="⏳")
    final_message.config(text="deciding...")

    window.after(2000, lambda: make_choice(a))

    
window.mainloop()
