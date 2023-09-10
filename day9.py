#from replit import clear
#from art import logo
#print(logo)


def win(bidders):
    winner = ""
    highest = 0
    for key in bidders:
        if bidders[key] > highest:
            winner = key
            highest = bidders[key]
    print(f"The winner is {winner} with a bid of ${str(highest)}")


bidders = {}
more = True

while more == True:
    user = input("What's your name? ")
    bid = int(input("What's your bid? $"))
    bidders = {user: bid}

    cont = input("Are there more bidders? y/n: ")
    if cont == 'y':
        more = True
    else:
        more = False
win(bidders)
