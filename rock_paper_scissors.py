import random

lst = ["rock", "scissors", "paper"]
choice = random.choice(lst)


uscore = 0
cscore = 0

def user_choice():
    print("enter rock, paper or scissors")
    user_choice = input("enter your choice --> ")
    if user_choice in lst:
        return user_choice
    else:
        return "enter valid choice"

def game(uchoice, choice):
    global uscore
    global cscore

    if uchoice == "rock" and choice == "rock":
        uscore = uscore + 0
        cscore = cscore + 0
    elif uchoice == "rock" and choice == "paper":
        cscore += 1
    elif uchoice == "rock" and choice == "scissors":
        uscore += 1

    elif uchoice == "paper" and choice == "paper":
        uscore = uscore + 0
        cscore = cscore + 0
    elif uchoice == "paper" and choice == "scissors":
        cscore += 1
    elif uchoice == "paper" and choice == "rock":
        uscore += 1

    elif uchoice == "scissors" and choice == "scissors":
        uscore = uscore + 0
        cscore = cscore + 0
    elif uchoice == "scissors" and choice == "rock":
        cscore += 1
    elif uchoice == "scissors" and choice == "paper":
        uscore += 1

def result():
    if uscore == cscore:
        print("\n\n Draw \n\n")
    elif uscore > cscore:
        print("\n\n Winner User \n\n")
    elif uscore < cscore:
        print("\n\n Winner Computer \n\n")


n = 0

while(n<3):
    print("\n")
    uchoice = user_choice()
    game(uchoice, choice)
    n += 1
    print("\n")
    print("user --> " + uchoice)
    print("computer --> " + choice)
    print("User score --> " + str(uscore))
    print("Computer score --> " + str(cscore))

result()