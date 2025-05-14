from os import system
repeating = ""
dictionary = {}
while repeating != "no":
    system("clear")
    # TODO-1: Ask the user for input
    name = input("What's your name? ")
    price = int(input("What's your bid? "))
    dictionary[name] = price

    repeating = input("Are there any other bidders?")

highest_bid = 0
for bidder in dictionary:
    bid_amount = dictionary[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
print(highest_bid,bidder)
