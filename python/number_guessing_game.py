import random
number_to_guess = random.randint(1, 100)
print("Welcome to the Number Guessing Game!")
print(number_to_guess)

number_of_attempts=10
while number_of_attempts>=1:
    guessed_number=int(input("Guess a number between 1 and 100: "))
    number_of_attempts-=1
    if guessed_number==number_to_guess:
        print("You guessed it right!")
    elif guessed_number-number_to_guess<=5 and number_to_guess-guessed_number<=5:
        print("You are very close!")
    elif guessed_number-number_to_guess>5:
        print("You are too high!")
    elif number_to_guess-guessed_number>5:
        print("You are too low!")
    number_of_attempts-=1
    print(f"You have {number_of_attempts} attempts left")
