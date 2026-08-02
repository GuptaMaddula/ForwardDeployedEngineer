

bids = {}
bidding_finished = False

highest_bid = 0
while not bidding_finished:
    print("Any bidders? Type 'yes' or 'no'.")
    answer = input().lower()
    if answer == "yes":
        name = input("What is your name? ")
        bid_amount = int(input("What is your bid? $"))
        bids[name] = bid_amount 
        if bid_amount > highest_bid:
            highest_bid = bid_amount
        print("\n"*50)
    else:
        bidding_finished = True
        print(f"{name} is the winner with a bid of ${highest_bid}.")
