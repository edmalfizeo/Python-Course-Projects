import random
import Hangman_Words
import Hangman_Art

choosen_word = random.choice(Hangman_Words.word_list)

word_list_blank = []

lives = 6

print(Hangman_Art.logo)

for letter in choosen_word: 
    word_list_blank += "_"

end_game = False
while not end_game: 
    guess = input("Guess a letter: ").lower() 
    if guess in word_list_blank:
        print(f"You already guessed {guess}")
        
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == guess:
            word_list_blank[position] = guess      
    print(word_list_blank)
    

    if "_" not in word_list_blank:
        end_game = True
        print("You Won The Game!!")

    if guess not in choosen_word:
        print(f"You guessed the letter {guess} and it is not in the choosen word!")
        lives -= 1
        if lives == 0:
            end_game = True
            print(f"The word was {choosen_word}. You Lost The Game!!")

    print(Hangman_Art.stages[lives])