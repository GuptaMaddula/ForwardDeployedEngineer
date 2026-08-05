import random

def my_game(): 
    cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    my_cards=[random.choice(cards), random.choice(cards)]
    print(f"Your cards are: {my_cards}")
    computer_cards=[random.choice(cards), random.choice(cards)]
    print(f"Computer's cards are: {computer_cards}, Computer's first card: {computer_cards[0]}")

    def calculate_score(cards):
        sum=0
        for card in my_cards:
            sum+=card
        return sum

    def calculate_score_computer(cards):
        sum=0
        for card in computer_cards:
            sum+=card
        return sum

    def check_win_or_lose():
        if calculate_score_computer(computer_cards)>calculate_score(my_cards) and calculate_score_computer(computer_cards)<=21:
            print("You lose!")
        elif calculate_score_computer(computer_cards)==calculate_score(my_cards):
            print("It's a draw!")
        else:
            print("You win!") 
    

    your_score=calculate_score(my_cards)
    computer_score=calculate_score_computer(computer_cards)

    print(f"Your score: {your_score}, computer's score: {computer_score}")

    continue_game=input("Type 'y' to get another card, type 'n' to pass: ")
    if continue_game=="y":
        my_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        your_score=calculate_score(my_cards)
        computer_score=calculate_score_computer(computer_cards)
        print(f"Your cards are: {my_cards}, current score: {your_score}")
        print(f"Computer's cards are: {computer_cards}, current score: {computer_score}")
        if calculate_score_computer(computer_cards)<calculate_score(my_cards) and calculate_score(my_cards)<=21:
            print("You lose!")
        elif calculate_score_computer(computer_cards)==calculate_score(my_cards):
            print("It's a draw!")
        else:
            print("You win!") 
    else:
        if calculate_score_computer(computer_cards)<17:
            computer_cards.append(random.choice(cards))
            print(f"Computer's cards final: {computer_cards}, final score: {calculate_score_computer(computer_cards)}")
            calculate_score_computer(computer_cards)
            check_win_or_lose()
        else:
            print(f"Computer's cards final: {computer_cards}, final score: {calculate_score_computer(computer_cards)}")
            check_win_or_lose()




def optimised():


    def deal_card():
        cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        return random.choice(cards)

    def calculate_score(cards):
        if sum(cards)==21 and len(cards)==2:
            return 0
        if 11 in cards and sum(cards)>21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score==computer_score:
            return "Draw"
        elif computer_score==0:
            return "Lose, opponent has Blackjack"
        elif user_score==0:
            return "Win with a Blackjack"
        elif user_score>21:
            return "You went over. You lose"
        elif computer_score>21:
            return "Opponent went over. You win"
        elif user_score>computer_score:
            return "You win"
        else:
            return "You lose"
    
    def play_game():
        user_cards=[]
        computer_cards=[]
        user_score=-1
        computer_score=-1
        is_game_over=False

        for _ in range(2):
            user_cards.append(deal_card())
            computer_cards.append(deal_card())

        while not is_game_over:
            user_score=calculate_score(user_cards)
            computer_score=calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score==0 or computer_score==0 or user_score>21:
                is_game_over=True
            else:
                user_should_continue=input("Type 'y' to get another card, type 'n' to pass: ")
                if user_should_continue=="y":
                    user_cards.append(deal_card())
                else:
                    is_game_over=True

        while computer_score!=0 and computer_score<17:
            computer_cards.append(deal_card())
            computer_score=calculate_score(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))

    while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")=="y": 
        print("\n"*50)
        play_game()

optimised()