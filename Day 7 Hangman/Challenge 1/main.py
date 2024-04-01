import random

word_list = ["ardvark", "baboon", "camel"]

random_word = random.choice(word_list)

letter = input("Guess a letter: ").lower()


for letters in random_word:
    if letter in letters:
        print("Right")
    else: 
        print("Wrong")    