class Card:
    def __init__(self, rank, suit, icon):
        self.rank = rank
        self.suit = suit
        self.icon = icon

    def getCardValue(self, low=True, high=False):
        if self.rank in range(2, 11):
            return self.rank
        elif self.rank > 10:
            return 10
        else:
            return 1 * low + 11 * high

    def __str__(self):
        high = 'JQK'
        if self.rank - 10 > 0:
            return high[self.rank - 11] + self.suit
        elif self.rank == 1:
            return 'A' + self.suit
        else:
            return str(self.rank) + self.suit

