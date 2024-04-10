import random, Art

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card(): 
    return random.choice(cards)

def calculate_score(hand):
    if len(hand) == 2 and 11 in hand and 10 in hand:
        return 0
    
    score = sum(hand)

    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)
        score = sum(hand)
    return score    
    
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Computer has a Blackjack. You lose!"
    elif user_score == 0:
        return "You have a Blackjack. You win!"
    elif user_score > 21:
        return "You went over. You lose!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"

def play_blackjack():
    user_cards = []
    computer_cards = []

    print(Art.logo)
    
    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
        print(compare(user_score, computer_score))
        return
    
    # User's turn
    while input("Do you want to draw another card? Type 'y' or 'n': ").lower() == 'y':
        user_cards.append(deal_card())
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        if user_score == 0 or user_score > 21:
            print(compare(user_score, computer_score))
            return

    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score)) 