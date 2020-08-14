class Profile(object):
    def __init__(self):
        self.hand = []
        self.value = 0

    def addCard(self, card):
        self.hand.append(card)

    def getHandValue(self):
        value = [0, 0]
        for card in self.hand:
            if card.rank == 1:
                value = [value[0] + 1, value[1] + 11]
            else:
                value = [value[0] + card.getCardValue(), value[1] + card.getCardValue()]
        self.value = value
        return value

    def hasAce(self):
        for card in self.hand:
            if card.rank == 1:
                return True
        return False

    def can_first_hit(self):
        return self.getHandValue()[0] < 21

    def can_second_hit(self):
        return self.getHandValue()[1] < 21

class User(Profile):
    def __init__(self):
        super().__init__()
        self.balance = 5000

    def place_bet(self, x):
        if self.balance > x:
            self.balance -= x

    def add_money(self, x):
        self.balance += x

class Dealer(Profile):
    def __init__(self):
        super().__init__()

    def stopPlaying(self):
        return self.getHandValue() >= 17
