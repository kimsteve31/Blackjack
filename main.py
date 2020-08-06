import pygame
from game import Blackjack
from pygame_widgets import Slider, TextBox
from widget import Button

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
DECK_X = 110
DECK_Y = 0

# Colors
white = (255, 255, 255)
green = (0, 128, 0)
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

# Load images
blueCard = pygame.transform.scale(pygame.image.load('PNG/z_blue.png'), (100, 150))
grayCard = pygame.transform.scale(pygame.image.load('PNG/z_gray.png'), (100, 150))
greenCard = pygame.transform.scale(pygame.image.load('PNG/z_green.png'), (100, 150))
userIcon = pygame.transform.scale(pygame.image.load('PNG/user.png'), (100, 100))
dealerIcon = pygame.transform.scale(pygame.image.load('PNG/dealer.png'), (100, 100))

class Application(object):
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.win.fill(green)
        pygame.display.set_caption("Blackjack")
        self.main()

    def main(self):

        # Buttons for cards in home screen
        blue = Button(black, 145, 295, 110, 160)
        gray = Button(black, 295, 295, 110, 160)
        green = Button(black, 445, 295, 110, 160)

        # Custom Bet Input
        slider = Slider(self.win, 250, 250, 200, 40, min=1, max=500, step=1, handleRadius=25)
        outputText = TextBox(self.win, 315, 325, 70, 50, fontSize=30)

        # Buttons for Bet Selection
        minButton = Button(white, 190, 400, 100, 50, 'MIN')
        maxButton = Button(white, 410, 400, 100, 50, 'MAX')
        customButton = Button(white, 300, 400, 100, 50, "CUSTOM")

        back = ''
        state = 0

        # Game Class
        blackjack = Blackjack()
        user = blackjack.user
        dealer = blackjack.dealer

        run = True
        while run:
            events = pygame.event.get()
            for event in events:
                pos = pygame.mouse.get_pos()
                if event.type == pygame.QUIT:
                    run = False

                self.checkHover(blue, gray, green, minButton, maxButton, customButton, pos)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if state == 0:
                        if blue.isOver(pos):
                            back = pygame.transform.scale(blueCard, (80, 110))
                        elif gray.isOver(pos):
                            back = pygame.transform.scale(grayCard, (80, 110))
                        elif green.isOver(pos):
                            back = pygame.transform.scale(greenCard, (80, 110))
                        else:
                            break
                        state = 1
                        self.fade()
                        blackjack.deckOfCards.shuffle()
                    elif state == 1:
                        bet = 0
                        if minButton.isOver(pos):
                            bet = 1
                        elif maxButton.isOver(pos):
                            bet = 500
                        elif customButton.isOver(pos):
                            bet = slider.getValue()
                        else:
                            break
                        state = 2
                        blackjack.place_bet(bet)
                        blackjack.deal_start_cards()
                        self.display_first_cards(user, dealer, back)
                    elif state == 2:
                        pass
                    elif state == 3:
                        pass

            if state == 0:
                self.display_homescreen(blue, gray, green)
            elif state == 1:
                slider.listen(events)
                self.display_betting(user.balance, slider, outputText, minButton, maxButton, customButton, back)
            elif state == 2:
                self.display_game(blackjack, user, dealer, back)
            elif state == 3:
                pass
            pygame.display.update()

    def display_first_cards(self, user, dealer, back):
        self.reset_play()
        for i in range(5):
            if i == 0:
                self.win.blit(pygame.transform.scale(pygame.image.load('PNG/' + user.hand[0].icon), (80, 110)), (110, 350))
            elif i == 1:
                self.win.blit(back, (110, 150))
            elif i == 2:
                self.win.blit(pygame.transform.scale(pygame.image.load('PNG/' + user.hand[1].icon), (80, 110)), (145, 350))
            elif i == 3:
                self.win.blit(back, (145, 150))
            elif i == 4:
                self.win.blit(pygame.transform.scale(pygame.image.load('PNG/' + dealer.hand[0].icon), (80, 110)), (110, 150))
                self.win.blit(back, (145, 150))
            pygame.display.update()
            pygame.time.delay(200)

    def reset_play(self):
        fill_board = pygame.Surface((SCREEN_WIDTH, 400))
        fill_board.fill(green)
        self.win.blit(fill_board, (0, 150))

    def display_game(self, jack, user, dealer, back):
        self.reset_play()

        if jack.turn == 'user':
            dX, dY = 110, 150
            self.win.blit(pygame.transform.scale(pygame.image.load('PNG/' + dealer.hand[0].icon), (80, 110)), (110, 150))
            self.win.blit(back, (145, 150))

        uX, uY = 110, 350
        for uCard in user.hand:
            self.win.blit(pygame.transform.scale(pygame.image.load('PNG/' + uCard.icon), (80, 110)), (uX, uY))
            uX += 35

    def checkHover(self, blue, gray, green, minb, maxb, cusb, pos):
        if blue.isOver(pos):
            blue.changeColor()
        elif gray.isOver(pos):
            gray.changeColor()
        elif green.isOver(pos):
            green.changeColor()
        else:
            blue.revertColor()
            gray.revertColor()
            green.revertColor()

        if minb.isOver(pos):
            minb.changeColor()
        elif maxb.isOver(pos):
            maxb.changeColor()
        elif cusb.isOver(pos):
            cusb.changeColor()
        else:
            minb.revertBetColor()
            maxb.revertBetColor()
            cusb.revertBetColor()

    def fade(self):
        fade = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        fade.fill(green)
        for alpha in range(0, 300, 2):
            fade.set_alpha(alpha)
            self.win.blit(fade, (0, 0))
            pygame.display.update()
            pygame.time.delay(5)

    def display_betting(self, balance, slider, outputText, minButton, maxButton, customButton, back):
        font = pygame.font.SysFont('comicsans', 30)

        waiting = font.render('WAITING FOR BETS', 1, black)
        text = font.render('$ ' + str(balance), 1, yellow)
        minbet = font.render('MIN', 1, black)
        minnum = font.render('$ 1', 1, black)
        maxnum = font.render('$ 500', 1, black)
        maxbet = font.render('MAX', 1, black)
        bal_text = font.render('BALANCE: ', 1, black)

        self.win.fill(green)
        self.decks(back)
        slider.draw()
        outputText.setText(slider.getValue())
        outputText.draw()
        minButton.draw(self.win, True)
        maxButton.draw(self.win, True)
        customButton.draw(self.win, True)
        self.win.blit(minbet, (175, 250))
        self.win.blit(minnum, (175, 275))
        self.win.blit(maxbet, (480, 250))
        self.win.blit(maxnum, (480, 275))
        self.win.blit(waiting, ((SCREEN_WIDTH // 2) - (waiting.get_width() // 2), 200))
        self.win.blit(bal_text, (10, 670))
        self.win.blit(text, (bal_text.get_width() + 10, 670))
        self.win.blit(userIcon, (600, 600))
        self.win.blit(dealerIcon, (5, 5))

    def decks(self, back):
        self.win.blit(back, (DECK_X, DECK_Y))

    def display_homescreen(self, blue, gray, green):
        fontE = pygame.font.SysFont('Elephant', 80)
        font = pygame.font.SysFont('Elephant', 30)
        title = fontE.render('BLACKJACK', 1, black)
        self.win.blit(title, (80, 80))

        blue.draw(self.win)
        gray.draw(self.win)
        green.draw(self.win)

        self.win.blit(blueCard, (150, 300))
        self.win.blit(grayCard, (300, 300))
        self.win.blit(greenCard, (450, 300))

        start = font.render('Click Card to Begin Game!', 1, black)
        self.win.blit(start, (150, 500))

if __name__ == '__main__':
    app = Application()
