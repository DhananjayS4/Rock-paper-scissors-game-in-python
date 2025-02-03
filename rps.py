import random 
import time
user_count= 0
computer_count=0
options=["rock","paper","scissors"]

while(True):
    user_input=input("Type Rock/ Paper or Scissors. Q to quit the game.\n").lower()
    if user_input=='q':
        print("Thank you for playing! This window will automatically close in 5 seconds.")
        time.sleep(5)
        break
    elif user_input not in options:
        print("Plese enter the valid option: ")
        continue 

    random_number=random.randint(0,2)
    computer_choice=options[random_number]
    print("Computer choice: ",computer_choice,".")

    if user_input==computer_choice:
        print("It's a tie!")
        user_count+=1
        computer_count+=1

    elif (user_input=='rock' and computer_choice=='scissors') or (user_input=='scissors' and computer_choice=='paper') or (user_input=='paper' and computer_choice=='rock'):
        print("You win!")
        user_count+=1
    else:
        print("Computer Won!")
        computer_count+=1

    print("You won ",user_count," times.")
    print("Computer won ",computer_count," times.")
    print("Well played!")