print("Welcome to the YoursPizza")
size = input("What size pizza do you want? S, M, or L ")


small_pizza = 15
medium_pizza = 20
large_pizza = 25

if size == "S":
    pepparoni = input("Do you want pepparoni? Y or N ")
    if pepparoni == "Y":
        bill=small_pizza+2
        Extra_cheese = input("Do you want extra cheese? Y or N ")
        if Extra_cheese == "Y":
            bill=bill+1
            print(f"Your total bill is: Rs{bill}")
       
    else:
        Extra_cheese = input("Do you want extra cheese? Y or N ")
        if Extra_cheese == "Y":
            bill=small_pizza+1
            print(f"Your total bill is: Rs{bill}")
        else:
            bill=small_pizza
            print(f"Your total bill is: Rs{bill}")

elif size == "M":
    pepparoni = input("Do you want pepparoni? Y or N ")
    if pepparoni == "Y":
        bill=medium_pizza+3
        Extra_cheese = input("Do you want extra cheese? Y or N ")
        if Extra_cheese == "Y":
            bill=bill+1
            print(f"Your total bill is: Rs{bill}")
        print(f"Your total bill is: Rs{bill}")
    else:
        Extra_cheese = input("Do you want extra cheese? Y or N ")
        if Extra_cheese == "Y":
            bill=medium_pizza+1
            print(f"Your total bill is: Rs{bill}")
        else:
            bill=medium_pizza
            print(f"Your total bill is: Rs{bill}")

elif size == "L":
    pepparoni = input("Do you want pepparoni? Y or N ")
    if pepparoni == "Y":
        bill=large_pizza+3
        Extra_cheese = input("Do you want extra cheese? Y or N ")
        if Extra_cheese == "Y":
            bill=bill+1
            print(f"Your total bill is: Rs{bill}")
        print(f"Your total bill is: Rs{bill}")
    else:
        Extra_cheese = input("Do you want extra cheese? Y or N ")
        if Extra_cheese == "Y":
            bill=large_pizza+1
            print(f"Your total bill is: Rs{bill}")
        else:
            bill=large_pizza
            print(f"Your total bill is: Rs{bill}")


else:
    print("Invalid input")