from profile import User, Dealer
from deck import Deck

class Blackjack(object):
    def __init__(self):
        self.user = User()
        self.dealer = Dealer()
        self.deckOfCards = Deck()
        self.turn = 'user'
        self.bet = 0

    def initate_game(self):
        self.deckOfCards.shuffle()

    def place_bet(self, bet):
        self.bet = bet

    def deal_start_cards(self):
        self.user.addCard(self.deckOfCards.removeTop())
        self.dealer.addCard(self.deckOfCards.removeTop())
        self.user.addCard(self.deckOfCards.removeTop())
        self.dealer.addCard(self.deckOfCards.removeTop())

    def hit(self):
        pass

    def can_hit(self):
        pass

    def stand(self):
        pass

    def can_split(self):
        pass

    def split(self):
        pass





