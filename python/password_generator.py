import random

print("Welcome to the Password Generator!")

letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
password=[]
length = int(input("How many characters would you like in your password?\n"))
letter = int(input("How many letters would you like in your password?\n"))
if(letter>length-2):
    print("You cannot have more letters than the total length minus 2 (for at least one number and one symbol). Please try again.")
    exit()
else:
    for i in range(1, letter+1):
        password.append(random.choice(letters))
    number = int(input("How many numbers would you like in your password?\n"))
    if(number>length-letter-1):
        print("You cannot have more numbers than the total length minus the number of letters minus 1 (for at least one symbol). Please try again.")
        exit()
    else:
        for i in range(1, number+1):
            password.append(random.choice(numbers))
        symbol = int(input("How many symbols would you like in your password?\n"))
        if(length==letter+number+symbol):
            for i in range(1, symbol+1):
                password.append(random.choice(symbols))
        else:
            print("The total number of letters, numbers, and symbols does not equal the desired password length. Please try again.")
            exit()

print("Your password will be generated now.")
    
print(f"Your password is: {password}")
your_password=""
random.shuffle(password)
print(f"Your password after shuffling is: {password}")
for char in password:
    your_password+=char


print(f"Your final password is : {your_password}")

