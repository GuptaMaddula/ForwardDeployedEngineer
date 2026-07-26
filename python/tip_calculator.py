print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? Rs"))
tip_percentage = float(input("What percentage tip would you like to give? "))
split = int(input("How many people to split the bill? "))

tip_amount = tip_percentage/100
split_bill = (total_bill + (total_bill * tip_amount)) / split
print(f"Each person should pay: Rs{split_bill:.2f}")