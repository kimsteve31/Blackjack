class Profile(object):
    def __init__(self):
        self.hand = []
        self.value = 0

    def addCard(self, card):
        self.hand.append(card)

    def getHandValue(self):
        value = 0
        for card in self.hand:
            value = value + card.getCardValue()
        self.value = value
        return value

class User(Profile):
    def __init__(self):
        super().__init__()
        self.balance = 5000

class Dealer(Profile):
    def __init__(self):
        super().__init__()

    def stopPlaying(self):
        return self.getHandValue() >= 17
