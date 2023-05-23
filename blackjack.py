############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = {
##    "A": [1,11],
##    "2": 2,
##    "3": 3,
##    "4": 4,
##    "5": 5,
##    "6": 6,
##    "7": 7,
##    "8": 8,
##    "9": 9,
##    "10": 10,
##    "J": 10,
##    "Q": 10,
##    "K": 10
##}
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

import random
from blackjackArt import logo

print(logo)
endGame = False
money = 2000
cards = {
    "A": [1,11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}

def getCard(pS):
    card = random.choice(list(cards.items()))
    cardShow = card[0]
    if cardShow == "A":
        if pS > 10:
            cardValue = card[1][0]
        else:
            cardValue = card[1][1]
    else:
        cardValue = card[1]
    return cardShow,cardValue

def playerDeal(money, bets):
    print("Player")
    playerSum = 0
    cardShow, cardValue = getCard(playerSum)
    print(cardShow, end=",")
    playerSum += cardValue
    cardShow, cardValue = getCard(playerSum)
    print(cardShow)
    playerSum += cardValue
    print(playerSum)
    if playerSum == 21:
        print("Player Win")
        money += bets
        print(money, "$")
        return True, playerSum, money
    else:
        return False, playerSum, money

def dealerDeal(money, bets):
    print("Dealer")
    dealerSum = 0
    cardShow, cardValue = getCard(dealerSum)
    print("_", end=",")
    dealerSum += cardValue
    cardShow, cardValue = getCard(dealerSum)
    print(cardShow)
    dealerSum += cardValue
    print(dealerSum)
    if dealerSum == 21:
        print("Dealer Win")
        money -= bets
        print(money, "$")
        return True, dealerSum, money
    else:
        return False, dealerSum, money

def hit(pS, dS, money, bets):
    pcardShow, pcardValue = getCard(pS)
    print(pcardShow)
    pS += pcardValue
    dcardShow, dcardValue = getCard(dS)
    print(dcardShow)
    dS += dcardValue
    if ((pS > 21) and (dS <= 21)) or ((dS == 21 and pS < 21)):
        money -= bets
        print(f"Dealer Win!: player {pS} --- dealer {dS}")
        print(money, "$")
        return 0, 0, money
    elif ((dS > 21) and (pS <= 21)) or ((pS == 21 and dS < 21)):
        money += bets
        print(f"Player Win!: player {pS} --- dealer {dS}")
        print(money, "$")
        return 0, 0, money
    elif (dS > 21) and (pS > 21):
        print(f"Push: player {pS} --- dealer {dS}")
        print(money, "$")
        return 0, 0, money
    else:
        return pS, dS, money

def stand(pS, dS, money, bets):
    if pS > dS:
        dcardShow, dcardValue = getCard(dS)
        print(dcardShow)
        dS += dcardValue
        if (pS > dS) or (dS > 21):
            money += bets
            print(f"Player Win!: player {pS} --- dealer {dS}")
            print(money, "$")
            return money
        elif pS == dS:
            print(f"Push: player {pS} --- dealer {dS}")
            print(money, "$")
            return money
        else:
            money -= bets
            print(f"Dealer Win!: player {pS} --- dealer {dS}")
            print(money, "$")
            return money
    elif pS < dS:
        money -= bets
        print(f"Dealer Win!: player {pS} --- dealer {dS}")
        print(money,"$")
        return money
    else:
        print(f"Push: player {pS} --- dealer {dS}")
        print(money, "$")
        return money

while not endGame:

    try:
        bets = int(input("Place your bets, if you want to stop then press '0': "))
        if bets == 0:
            break
    except ValueError:
        print('You have input number...')
        continue
    pWin, pSum, money = playerDeal(money, bets)
    dWin, dSum, money = dealerDeal(money, bets)
    if pWin or dWin:
        continue
    else:
        while 1:
            option = input("Hit or Stand?: ").lower()
            if option == "hit":
                pSum, dSum, money = hit(pSum, dSum, money, bets)
                if pSum == dSum == 0:
                    break
                else:
                    continue
            elif option == "stand":
                money = stand(pSum, dSum, money, bets)
                break
            else:
                continue

