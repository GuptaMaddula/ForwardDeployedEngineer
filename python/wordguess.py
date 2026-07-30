import random
words_list = ["python", "java", "javascript", "ruby", "swift", "kotlin", "typescript", "go", "rust", "perl"]

word = random.choice(words_list)
print(f"The word to guess is: {word}")  # For testing purposes, you can remove this line in production
print("Welcome to the Word Guessing Game!")

placeholder =""
for chars in word:
    placeholder+="_"
print(placeholder)
print("Guess a letter in the word.")

letter = str(input("guess a letter: ")).lower()
guessed_word=""

for char in word:
    if char == letter:
        print(letter)
        guessed_word+=letter
    else:
        guessed_word+="_"

print(guessed_word)