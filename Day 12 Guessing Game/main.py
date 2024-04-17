import random 
from Art import art

lives = 0

print(art)

print("-" * 10)
print("Welcome to the Guessing Game!")
print("I will choose a number between 1 to 100, can you guess it?")
print("-" * 10)

difficulty = input("\nPlease choose a difficulty: [easy/hard]?")

if difficulty == 'hard': 
        lives = 5
        random_number = random.randint(1, 100)
        while lives > 0:
            number = int(input("Guess a number: ")) 
            if number == random_number:
                print(f"Congratulations you guess it right! The number was {random_number}")
                break
            if number < random_number:
                print("To low!")
                lives -= 1
            if number > random_number:
                print("To high!")
                lives -= 1    
            if lives == 0:
                print(f"The number was {random_number}")    

if difficulty == 'easy': 
        lives = 10
        random_number = random.randint(1, 100)
        while lives > 0:
            number = int(input("Guess a number: "))
            if number == random_number:
                print(f"Congratulations you guess it right! The number was {random_number}")
                break
            if number < random_number:
                print("To low!")
                lives -= 1
            if number > random_number:
                print("To high!")
                lives -= 1    
            if lives == 0:
                print(f"The number was {random_number}")     
