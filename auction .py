from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
bids={}
bidding_finished=False
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"the winner is {winner}with a {highest_bid}")        
while not bidding_finished:
    name=input("what is ure name")
    price=int(input("what is ure price "))
    bids[name]=price
    should_continue=input(" are there any other bidders ?'type yes or no'.\n")
    if should_continue=="no":
        bidding_finished=True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear()
