print("Welcome to the YoursPizza")
size = input("What size pizza do you want? S, M, or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0


if size == "S":
    bill = 15
elif size == "M":
    bill = 20   
elif size == "L":
    bill = 25
else:
    print("Invalid input")

if pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M" or size == "L":
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your total bill is: ${bill}")