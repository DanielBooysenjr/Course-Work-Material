print("Welcome to the silent bidding program")

bidder_information = {}
other_bidders = True

def finding_highest_bid(bidder_information):
    highest_bid = 0
    winner = ""

    # {Daniel}: 2838 {Faith}: 8273

    for bidder in bidder_information:
        bid_amount = bidder_information[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder

    print(f"Winner is {winner} with bid of ${highest_bid}")

while other_bidders == True:
    bidder_name = input("What is your name? ")
    bid_amount = int(input("How much would you like to bid? $"))
    bidder_information[bidder_name] = bid_amount
    other_bidders = input("Are there any other bidders? ").lower()

    if other_bidders != "yes":
        other_bidders = False
        finding_highest_bid(bidder_information)
    else:
        other_bidders = True


    

