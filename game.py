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
        self.user.place_bet(bet)

    def take_out_bet(self, won):
        if won:
            self.user.add_money(self.bet * 2)
            self.bet = 0

    def deal_start_cards(self):
        self.user.addCard(self.deckOfCards.removeTop())
        self.dealer.addCard(self.deckOfCards.removeTop())
        self.user.addCard(self.deckOfCards.removeTop())
        self.dealer.addCard(self.deckOfCards.removeTop())

    def hit(self):
        if len(self.user.hand) <= 10 and self.user.can_first_hit():
            self.user.addCard(self.deckOfCards.removeTop())

    def stand(self):
        pass

    def split(self):
        pass





