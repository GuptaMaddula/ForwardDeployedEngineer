import random

list=["stone", "paper", "scissors"]
print("Welcome to the game of Stone, Paper, Scissors!")
user_choice = input("Enter your choice (stone, paper, scissors): ")
computer_choice = random.choice(list)
if user_choice not in list:
    print("Invalid input. Please choose stone, paper, or scissors.")
elif(user_choice == computer_choice):
    print(f"Both players selected {user_choice}. It's a tie!")
elif(user_choice == "stone" and computer_choice == "scissors"):
    print(f"Stone smashes scissors! You win!")
elif(user_choice == "paper" and computer_choice == "stone"):
    print(f"Paper covers stone! You win!")
elif(user_choice == "scissors" and computer_choice == "paper"):
    print(f"Scissors cuts paper! You win!")
else:
    print(f"{computer_choice} beats {user_choice}! You lose.")