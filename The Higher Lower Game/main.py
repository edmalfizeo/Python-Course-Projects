import art, game_data, random
def game():
    should_continue = ""
    lives = 5
    print(art.logo)
    print("Welcome to The Higher Lower Game\n")
    print("The rules are simple, guess who was more searchs on internet!\n")
    while should_continue != "N" or lives != 0:
        choise1 = game_data.data[random.randint(0, len(game_data.data) - 1)]
        choise2 = game_data.data[random.randint(0, len(game_data.data) - 1)]
        print(f"A - name: {choise1['name']}, description: {choise1['description']}   vs   B - name: {choise2['name']}, description: {choise2['description']}")
        if choise1 == choise2:
            print("Tie, the computer choose equal")
        guess = input("What is your guess? [A/B]: ").upper()
        if guess == 'A' and choise1['follower_count'] > choise2['follower_count']:
            print("Congrats! You win!")
        elif guess == 'B' and choise2['follower_count'] > choise1['follower_count']:
            print("Congrats! You win!")
        else:
            lives -= 1
            print("Sorry, you lose!")
            print(lives)
            if lives == 0:
                print("You lost all the lives! Thanks for playing!")
                break
        should_continue = input("Would you like to play again? [Y/N]:").upper()





game()