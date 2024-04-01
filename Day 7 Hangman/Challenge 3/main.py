import random

word_list = ["ardvark", "baboon", "camel"]

choosen_word = random.choice(word_list)

word_list_blank = []
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

for letter in choosen_word: 
    word_list_blank += "_"

end_game = False
while not end_game: 
    guess = input("Guess a letter: ").lower() 
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            word_list_blank[position] = guess  
    print(word_list_blank)
    

    if "_" not in word_list_blank:
        end_game = True
        print("You Won The Game!!")

    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_game = True
            print("You Lost The Game!!")

    print(stages[lives])        