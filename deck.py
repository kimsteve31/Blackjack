import os
from card import Card
from random import randrange

deckSize = 208

class Deck(object):
    def __init__(self):
        self.shoe = []
        self.shield = []
        self.createDeck()

    def createDeck(self):
        suits = 'CDHS'
        for i in range(4):
            for rank in range(1, 14):
                for suit in suits:
                    if rank in range(2, 11):
                        addCard = Card(rank, suit, str(rank) + suit + '.png')
                    elif rank == 1:
                        addCard = Card(rank, suit, 'A' + suit + '.png')
                    elif rank == 11:
                        addCard = Card(rank, suit, 'J' + suit + '.png')
                    elif rank == 12:
                        addCard = Card(rank, suit, 'Q' + suit + '.png')
                    else:
                        addCard = Card(rank, suit, 'K' + suit + '.png')
                    self.addToTop(addCard)

    def shuffle(self):
        for index in range(deckSize - 1, 0, -1):
            replace = randrange(index+1)
            self.shoe[index], self.shoe[replace] = self.shoe[replace], self.shoe[index]

    def collect_cards(self, user, dealer):
        self.shield += user
        self.shield += dealer
        self.reshuffle()

    def addToTop(self, addCard):
        """
        The top is referenced at the end of the card stack
        :param addCard: Card to be added to the stack
        :return: None
        """
        self.shoe.append(addCard)

    def removeTop(self):
        """
        The top is referenced at the end of the card stack
        :return: The card that was removed
        """
        return self.shoe.pop()

    def getShoeSize(self):
        return len(self.shoe)

    def getShieldSize(self):
        return len(self.shield)

    def reshuffle(self):
        if self.getShieldSize() + self.getShoeSize() == deckSize and self.getShieldSize() >= (208 // 2):
            self.shoe.extend(self.shield)
            self.shuffle()
            self.shield = []


"""
dk = Deck()
dk.shuffle()
cd = dk.cards
for c in cd:
    print(c.__str__())
"""

