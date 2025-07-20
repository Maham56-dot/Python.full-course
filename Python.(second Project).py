proj2="Dice Roller Simulator in Python"
import random
def roll_dice():  #simulate the roll of a dice and return the result
    return random.randint(1,6)
def main():
    print("Welcome to the Dice Roller Simulator!")
    while True:
        input("press enter to the roll the dice...")
        result = roll_dice()
        print(f"you rolled a {result}")
        user_input=input("Roll again?(y/n):")
        if user_input.lower()!='y':
            print("Thanks for playing!")
            break
        #call the main function to start the program
main()        