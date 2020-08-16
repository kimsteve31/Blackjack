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

    def place_bet(self, bet, double=False):
        self.user.place_bet(bet)
        if double:
            bet = bet * 2
        self.bet = bet

    def get_pot(self):
        return self.bet

    def handle_payout(self):
        stat = self.get_status()
        if stat == 'BLACKJACK' or stat == 'won' or stat == 'dealerbust':
            self.user.add_money(self.bet * 2)
            self.bet = 0

    def lost_bet(self):
        self.bet = 0

    def reset_game(self):
        self.deckOfCards.collect_cards(self.user.hand, self.dealer.hand)
        self.user.hand, self.dealer.hand = [], []
        self.set_status('reset')

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
                self.set_status('dealer')
                self.place_bet(self.bet, True)

    def set_status(self, status):
        self.turn = status

    def get_status(self):
        return self.turn

    def check_Busted(self):
        if self.user.getHandValue()[0] > 21:
            self.set_status('over')
        else:
            self.set_status('user')

    def check_blackjack(self):
        score = self.user.getHandValue()
        if score[0] == 21 or score[1] == 21:
            self.set_status('BLACKJACK')
            self.handle_payout()

    def compare_score(self):
        user_score = self.user.getHandValue()
        dealer_score = self.dealer.getHandValue()
        if dealer_score > 21:
            return True
        elif user_score[1] > 21:
            return user_score[0] > dealer_score
        else:
            return user_score[1] > dealer_score

    def double(self):
        self.hit(True)

    def stand(self):
        self.set_status('dealer')

    def dealer_play(self):
        if self.dealer.getHandValue() <= 16:
            self.dealer.addCard(self.deckOfCards.removeTop())

    def dealer_draw(self):
        return self.dealer.getHandValue() > 16

    def dealer_bust(self):
        return self.dealer.getHandValue() > 21

    def split(self):
        pass





