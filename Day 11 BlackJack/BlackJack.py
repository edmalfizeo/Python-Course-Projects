import random


def deal_card(): 
    return random.choice(cards)

def calculate_score():
    if result_player == 21 and result_computer != 21:
        return "Player Wins"
        should_continue = False
    elif result_computer == 21 and result_player != 21:
        return "Dealer Wins"
        should_continue = False
    elif result_player == 21 and result_computer == 21:
        return "Dealer Wins"
        should_continue = False
    elif result_player > 21 and 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
    elif result_computer > 21 and 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)
    elif result_player > 21:
        should_continue = False
    elif result_computer > 21:
        should_continue = False            

        
should_continue = True
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

user_cards.append(deal_card())
user_cards.append(deal_card())

computer_cards.append(deal_card())
computer_cards.append(deal_card())

result_player = sum(user_cards)
result_computer = sum(computer_cards)

while should_continue:
    print(f"User hand = {user_cards}, count accourage: {result_player}")
    print(f"Computer hand = {computer_cards}, count accourage: {result_computer}")
    print(calculate_score())
    should_continue = False

    
    


