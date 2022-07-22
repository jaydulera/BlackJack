import itertools
from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
    
    def getCards(self):
        for product in itertools.product(Card.cards , Card.shapes):
            self.cards.append(Card(product[1] , product[0] , Card.cards_values[product[0]]))

    def printCards(self):
        for card in self.cards:
            print("{} of {} with value {}".format(card.card , card.shape , card.value))

    def draw(self):
        newCard =  random.choice(self.cards)
        self.cards.remove(newCard)
        return newCard

