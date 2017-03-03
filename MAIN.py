# 21 (Blackjack...Almost) - A game by Coderman64
from Deck import *

running = True

while running:
    mainDeck = Deck()
    mainDeck.shuffle()
    playerHand = []
    for i in range(2):
        playerHand.extend([mainDeck.drawTopCard()])
    for i in playerHand:
        print(i.getPrintableName())
    running = False