#Deck.py
# allows you to have a virtual deck from which you can draw cards
from random import shuffle

class Card:
    def __init__(self,number, suit):        
        self.number = number;
        self.suit = suit;
        #print("card created")
    def getPrintableName(self):
        possibleNumbers=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        relatedvalues = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        
        indexNumber = possibleNumbers.index(self.number.upper())
        cardName = relatedvalues[indexNumber]
        suitName = "no suit"
        if self.suit.lower() == 's':
            suitName = 'Spades'
        elif self.suit.lower() == 'h':
            suitName = 'Hearts'
        elif self.suit.lower() == 'd':
            suitName = 'Diamonds'
        elif self.suit.lower() == 'c':
            suitName = 'Clubs'
        return cardName+" of "+suitName
    def getValue(self):
        possibleNumbers=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        relatedvalues = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        
        indexNumber = possibleNumbers.index(self.number.upper())
        return relatedvalues[indexNumber]

class Deck:
    def __init__(self):
        self.resetDeck()
    def shuffle(self):
        shuffle(self.cards)
    def printCards(self):
        for c in self.cards:
            print(c.getPrintableName())
    def drawTopCard(self):
        return self.cards.pop(0)
    def resetDeck(self):
        possibleNumbers=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        possibleSuits = ['S','C','H','D']
        self.cards = []
        for s in possibleSuits:
            for n in possibleNumbers:
                self.cards.extend([Card(n,s)])