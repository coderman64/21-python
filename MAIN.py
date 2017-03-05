# 21 (Blackjack...Almost) - A game by Coderman64
from Deck import *
from time import sleep

waitTime = 1

def getPlayerValue(playerHand):
    playerValue = 0
    for i in playerHand:
        playerValue += i.getValue()
    if playerValue > 21:
        for i in playerHand:
            if i.getValue() == 11:
                playerValue -= 10
                if playerValue <= 21:
                    break
    return playerValue

def notifyHand(playerHand):
    for i in playerHand:
        print(i.getPrintableName())
    print("total value: "+str(getPlayerValue(playerHand)))
running = True
try:
    while running:
        mainDeck = Deck()
        mainDeck.shuffle()

        playerHand = []
        for i in range(2):
            playerHand.extend([mainDeck.drawTopCard()])

        dealerHand = []
        for i in range(2):
            dealerHand.extend([mainDeck.drawTopCard()])
        playing = True
        while playing:
            print("\n")
            print("you have:")
            notifyHand(playerHand)
            playerResponse = raw_input("What do you want to do? (type 'help' to show your options)\n> ")
            if playerResponse == "help":
                print("""---possible responses---
    help: show this help page
    hit: get another card from the deck
    stay: stick with your current hand""")
            elif playerResponse == "hit":
                newCard = mainDeck.drawTopCard()
                playerHand.extend([newCard])
                print("you just got a "+newCard.getPrintableName())
                sleep(waitTime)
                if getPlayerValue(playerHand) > 21:
                    print("you're bust!")
                    sleep(waitTime)
                    playing = False
            elif playerResponse == "stay":
                playing = False
            else:
                print("that was not a legitimate option, please try again.")
        print("\n")
        while getPlayerValue(dealerHand) < 17:
            newCard = mainDeck.drawTopCard()
            dealerHand.extend([newCard])
            print("the dealer just drew a "+newCard.getPrintableName())
            if getPlayerValue(dealerHand) > 21:
                sleep(waitTime)
                print("the dealer is bust!")
            sleep(waitTime)
        print("\nthe dealer has: ")
        notifyHand(dealerHand)
        sleep(waitTime)
        if (getPlayerValue(playerHand)>getPlayerValue(dealerHand) and getPlayerValue(playerHand) <= 21) or (getPlayerValue(dealerHand) > 21 and getPlayerValue(playerHand) <= 21):
            print("\nyou win!")
        elif (getPlayerValue(playerHand)<getPlayerValue(dealerHand) and getPlayerValue(dealerHand) <= 21) or (getPlayerValue(playerHand) > 21 and getPlayerValue(dealerHand) <= 21):
            print("\ndealer wins!")
        else:
            print("\ndraw!")
        print("")
        playPrompt = True
        sleep(waitTime)
        while playPrompt:
            playAgain = raw_input("do you want to play again? ('yes' or 'no')")
            if playAgain.lower() == "yes":
                playPrompt = False
            elif playAgain.lower() == "no":
                playPrompt = False
                running = False
                print("okay! Exiting...")
            else:
                print("please type 'yes' or 'no'")
except KeyboardInterrupt:
    print("stopping game...")
