import random

word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)


word_list_blank = []
for letter in choosen_word: 
    word_list_blank += "_"

print(word_list_blank) 

guess = input("Guess a letter: ").lower()

for position in range(len(choosen_word)):
    letter = choosen_word[position]
    if letter == guess:
        word_list_blank[position] = guess
print(word_list_blank)        