import random
words_list = ["python", "java", "javascript", "ruby", "swift", "kotlin", "typescript", "go", "rust", "perl"]

word = random.choice(words_list)
print(f"The word to guess is: {word}")  # For testing purposes, you can remove this line in production
print("Welcome to the Word Guessing Game!")

placeholder =""
for chars in word:
    placeholder+="_"
print(placeholder)
#guessed_word=""
lives=len(word)
game_over=False
correct_letters = []

while lives > 0:
    letter = str(input("guess a letter in the word: ")).lower()
   

    guessed_word=""
    for char in word:
        if char == letter:
            guessed_word+=letter
            correct_letters.append(letter)
        elif char in correct_letters:
            guessed_word+=char
        else:
            guessed_word+="_"

    print(guessed_word)
    if letter not in word:
        lives -= 1
        print(f"Incorrect guess. You have {lives} lives remaining.")
        if lives == 0:
            print("Game over! You've run out of lives.")
            game_over=True
            break

    if guessed_word == word:
        print("Congratulations! You've guessed the word correctly.")
        game_over=True
        break



 # if len(letter) != 1 or not letter.isalpha():
    #     print("Please enter a single alphabetic character.")
    #     continue