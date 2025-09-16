from os import system

def bidding_input():
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    return name, bid

def bidding(name, bid):
    global max_bid, winner
    bids[name] = bid
    if bid > max_bid:
        max_bid = bid
        winner = name

print("Welcome To the Bidding:")

bids = {}
max_bid = 0 
winner = ""

while True:
    name, bid = bidding_input()
    bidding(name, bid)
    
    if input("Do you want to continue bidding? (yes/no): ").lower() == "no":
        break
    system("clear")

print(f"The winner is {winner} with a bid of {max_bid}")
