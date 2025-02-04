import random 
import time
user_count= 0
computer_count=0
options=["rock","paper","scissors"]

cwin = ["Imaging losing XD", "What can I say, I'm just too good at this ;D", "You should just quit XD", "You'll catch up don't worry :3"]
uwin = ["I'll get there soon enough", "You just got lucky...", "Are you cheating???", "I'm reporting you >:(", "Are you a hacker?"]
draw = ["Jinx!", "Like minds think alike ;)","Should've gone with my gut feeling...", "déjà vu"]

def score():
        print("\n")
        print("Current score:")
        print("You\tComputer")
        print(f"{user_count}\t{computer_count}")
        print("\n")

print("Computer: Hello there! Let's play ^-^\n")

while(True):
  main
    user_input=input("Type Rock, Paper or Scissors. Type Q to exit the game.\n>> ").lower()

    if user_input=='q':
        print("Thank you for playing! This window will automatically close in 5 seconds.")
        print("Computer: This was fun! See you soon! ;)")
        time.sleep(5)
        break

    elif user_input=='score':
        score()
        continue

    elif user_input not in options:
        print("Invalid option. Try again.\n ")
        continue 

    computer_choice=random.choice(options)
    print(f"\nComputer chose {computer_choice.capitalize()}!")

    if user_input==computer_choice:
        print("It's a Draw!")
        print(f"\nComputer: {random.choice(draw)}\n")

    elif (user_input=='rock' and computer_choice=='scissors') or (user_input=='scissors' and computer_choice=='paper') or (user_input=='paper' and computer_choice=='rock'):
        print("You Win!")
        user_count+=1
        print(f"\nComputer: {random.choice(uwin)}\n")
    else:
        print("Computer Wins!")
        computer_count+=1
        print(f"\nComputer: {random.choice(cwin)}\n")