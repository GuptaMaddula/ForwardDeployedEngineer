import random

cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
my_cards=[random.choice(cards), random.choice(cards)]
computer_cards=[random.choice(cards), random.choice(cards)]

def calculate_score(cards):
    sum=0
    for card in my_cards:
        sum+=card
    print(f"Your cards are: {my_cards}, current score: {sum}")
    return sum

def calculate_score_computer(cards):
    sum=0
    for card in computer_cards:
        sum+=card
    print(f"Computer's first card: {computer_cards[0]}")
    return sum

calculate_score(my_cards)
calculate_score_computer(computer_cards)
continue_game=input("Type 'y' to get another card, type 'n' to pass: ")
if continue_game=="y":
    my_cards.append(random.choice(cards))

else:
    if calculate_score_computer(computer_cards)<17:
        computer_cards.append(random.choice(cards))
        print(f"Computer's cards are: {computer_cards}, current score: {calculate_score_computer(computer_cards)}")
        calculate_score_computer(computer_cards)
        if calculate_score_computer(computer_cards)>calculate_score(my_cards) and calculate_score_computer(computer_cards)<=21:
            print("You lose!")
        elif calculate_score_computer(computer_cards)==calculate_score(my_cards):
            print("It's a draw!")
        else:
            print("You win!")
    else:
        print(f"Computer's cards are: {computer_cards}, current score: {calculate_score_computer(computer_cards)}")
        if calculate_score_computer(computer_cards)>calculate_score(my_cards) and calculate_score_computer(computer_cards)<=21:
            print("You lose!")
        elif calculate_score_computer(computer_cards)==calculate_score(my_cards):
            print("It's a draw!")
        else:
            print("You win!")    