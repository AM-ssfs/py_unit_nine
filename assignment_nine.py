# Aden Menschik
# Last modified dec 16
# plays a standard game of "war" where two players start with equal amount of cards and compare the top card each turn
# the higher card wins both cards
# in case of a tie, 3 cards are added to the bounty and they compare again. higher card takes the bounty too
# game ends when one player is out of cards, the other player wins

# p1 = player1 deck
# p1l = player1 deck length
# p1c = player1's card
# p1v = player1 card value (rank)

from deck import Deck
from random import shuffle

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


# makes 2 equal sized decks of random cards
def deal_cards(deck):
    p1 = []
    p2 = []
    for x in range(26):
        p1.append(deck.deal())
    for y in range(26):
        p2.append(deck.deal())
    decks = [p1, p2]
    return decks


def compare(p1, p2):

    p1l = len(p1)-1
    p2l = len(p2)-1

    if p1l <= 0:
        return "PLAYER 2 WINS!"
    if p2l <= 0:
        return "PLAYER 1 WINS!"

    p1c = p1.pop(0)
    p2c = p2.pop(0)
    bounty = []

    print("player1: "+ str(p1c))
    print("player2: "+ str(p2c))
    p1v = ranks.index(p1c.rank)
    p2v = ranks.index(p2c.rank)

    # prevents rare error
    p1_error = ''
    p2_error = ''

    while p1v == p2v:

        if p1_error != p1c:
            bounty.append(p1c)
        if p2_error != p2c:
            bounty.append(p2c)
        for x in range(3):
            if len(p1)-1 >= 2:
                bounty.append(p1.pop(0))
        if p1:
            p1c = p1.pop(0)

        for x in range(3):
            if len(p2)-1 >= 2:
                bounty.append(p2.pop(0))
        if p2:
            p2c = p2.pop(0)

        p1v = ranks.index(p1c.rank)
        p2v = ranks.index(p2c.rank)
        print("")
        bounty_list = []
        for x in range(len(bounty)):
            bounty_list.append(bounty[x].rank + bounty[x].suit)
        print("bounty: " + str(bounty_list))
        print("")
        print(p1c)
        print(p2c)
        # prevents extremely rare error where p1 and p2 compare equal two or more times in a row on their last card
        if len(p1) == 0:
            p1_error = p1c
        if len(p2) == 0:
            p2_error = p2c
    if p1v > p2v:
        # prevents never ending games
        shuffle(p1)
        p1.append(p1c)
        p1.append(p2c)
        # if there is a bounty then it is added to the player's deck
        while bounty:
            p1.append(bounty.pop(0))

        print("p1 win")
    elif p2v > p1v:
        shuffle(p2)
        p2.append(p1c)
        p2.append(p2c)
        while bounty:
            p2.append(bounty.pop(0))
        print("p2 win")


    if (len(p1)+len(p2)+len(bounty)) < 52:
        print("card deleted somewhere!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        cause_an_error()  # this intentionaly creates an error so the program stops where it broke

    if (len(p1) + len(p2) + len(bounty)) > 52:
        print("card duplicated somewhere!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        cause_an_error()


def main():
    p1wins = 0
    p2wins = 0
    play_again = True
    while play_again == True:
        # I am able to run it many time so i find errors
        for x in range(1):
            deck = Deck()
            deck.shuffle()
            decks = deal_cards(deck)
            p1 = decks[0]
            p2 = decks[1]
            winner = False
            while not winner:
                winner = compare(p1, p2)
            print(winner)
            if winner == "PLAYER 2 WINS!":
                p2wins += 1
            elif winner == "PLAYER 1 WINS!":
                p1wins += 1
            print(str(p1wins) + " to " + str(p2wins))

        user_input = False
        while not user_input:  # until user answers correctly

            answer = input("do you want to play again? (y/n) ")
            print()

            if answer.upper() == "Y" or answer.upper() == "YES":
                print()
                play_again = True
                user_input = True

            elif answer.upper() == "N" or answer.upper() == "NO":
                print()
                play_again = False
                user_input = True

            else:
                print("please enter \"Y\", \"yes\", \"N\" or \"no\".")

    print("thank you for playing!")
    print("the final score was: " + str(p1wins) + " to " + str(p2wins))

if __name__ == '__main__':
    main()

