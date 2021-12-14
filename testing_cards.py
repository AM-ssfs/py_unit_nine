import deck
import card

new_deck = deck.Deck()

print(new_deck.cards[1].rank + " of " + new_deck.cards[1].suit)
print(new_deck.cards[1])

newcard = card.Card("Hearts", "4")
newercard = card.Card("Hearts", "8")

print(newcard)
if newercard > newcard:
    print("eee")
