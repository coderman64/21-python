# 21 (Blackjack...Almost) - A game by Coderman64
from Deck import *

running = True

while running:
    mainDeck = Deck()
    mainDeck.shuffle()
    playerHand = []
    for i in range(2):
        playerHand.extend([mainDeck.drawTopCard()])
    playerValue = 0
    for i in playerHand:
        print(i.getPrintableName())
        playerValue += i.getValue()
    print("your current hand is worth "+str(playerValue))
    running = False
