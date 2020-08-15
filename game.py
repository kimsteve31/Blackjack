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

    def handle_payout(self):
        if self.get_status() == 'BLACKJACK':
            self.user.add_money(self.bet * 2)
            self.bet = 0

    def reset_game(self):
        self.deckOfCards.collect_cards(self.user.hand, self.dealer.hand)
        self.user.hand, self.dealer.hand = [], []
        self.turn = 'reset'

    def deal_start_cards(self):
        self.user.addCard(self.deckOfCards.removeTop())
        self.dealer.addCard(self.deckOfCards.removeTop())
        self.user.addCard(self.deckOfCards.removeTop())
        self.dealer.addCard(self.deckOfCards.removeTop())

    def hit(self, double=False):
        if len(self.user.hand) <= 10 and self.user.can_first_hit():
            self.user.addCard(self.deckOfCards.removeTop())
            self.check_Busted()
            if double:
                self.turn = 'dealer'

    def new_game(self):
        self.turn = 'user'

    def check_Busted(self):
        if self.user.getHandValue()[0] > 21:
            self.turn = 'over'
        else:
            self.turn = 'user'

    def check_win(self):
        score = self.user.getHandValue()
        if score[0] == 21 or score[1] == 21:
            self.turn = 'BLACKJACK'
            self.handle_payout()

    def get_status(self):
        return self.turn

    def double(self):
        self.hit(True)

    def stand(self):
        self.turn = 'dealer'

    def split(self):
        pass





