import os
import art


end = False
list_auction = {}
highest_bid = 0
while not end:
    print(art.logo)
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))

    list_auction[name] = bid

    choosen_option = input("Do you want to add other person? [yes/no]: ").lower()

    if choosen_option == "yes":
        os.system("cls")
    elif choosen_option == "no":
        end = True
        os.system("cls")

for bidder in list_auction:
    bid_amount = list_auction[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"The highest bid was from {winner} with ${highest_bid:.2f}")
  
