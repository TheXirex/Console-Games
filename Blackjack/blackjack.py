import random

suits = ('♡', '♢', '♤', '♧')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10,'Q': 10, 'K': 10, 'A': 11}

play = True

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'|‾‾‾‾|\n| {self.rank}{self.suit} |\n|____|'

class Deck:

    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        pop_card = self.deck.pop()
        return pop_card

class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'A': self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1 

class Chips:
    
    def __init__(self, total):
        self.total = total
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def clear_console():

    print('\n' * 50)

def make_bet():

    while True:
        try:
            total = int(input('With what account would you like to sit at the table?\n'))
            if total < 0:
                print('The value must be greater than 0!')
                continue
        except:
            print('Wrong value! Enter an integer greater than zero!')
            continue
        else:
            return total

def take_bet(chips):

    print(f'You have {chips.total}$ in your account.')
    while True:
        try:
            chips.bet = int(input('Choose your bet: \n'))
        except:
            print('Wrong value! Enter an integer greater than zero!')
            continue
        else:
            if chips.bet <= chips.total:
                break
            else:
                print(f'Bet more than your account! You can bet a maximum of {chips.total}$.')
                continue

def hit(deck, hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):

    global play

    while True:
        answer = input('Choose hit (h) or stand (s): \n')
        if answer.lower() == 'h':
            hit(deck, hand)
        elif answer.lower() == 's':
            print('Player stands.')
            play = False
        else:
           print('Wrong answer! Try again.')
           continue
        break

def show_some(player,dealer):

    print(f"\nDealer's hand:\n")
    print("\n|‾‾‾‾|\n| ?? |\n|____|")
    print(dealer.cards[1])

    print(f"\nPlayer's hand:\n", *player.cards, sep='\n')
    print(f"\nPlayer's points: {player.value}")
    
def show_all(player,dealer):

    print("\nDealer's Hand:\n", *dealer.cards, sep='\n')
    print(f"\nDealer's points: {dealer.value}")

    print("\nPlayer's Hand:\n", *player.cards, sep='\n')
    print(f"\nPlayer's points: {player.value}")

def player_overcards(chips):

    print('The player overcards!')
    chips.lose_bet()

def player_win(chips):

    print('Player win!')
    chips.win_bet()

def dealer_overcards(chips):

    print('The dealer overcards!')
    chips.win_bet()

def dealer_win(chips):

    print('Dealer win!')
    chips.lose_bet()

def tie():

    print('Tie!')

def init():

    print('\n\nWelcome to Blackjack!'
          '\nPlaying by the classic rules: card values from Jack to King are 10,' 
          '\nAce 1 or 11, the other cards are at face value;'
          '\nthe dealer does not take cards at 17 or more points.'
          '\nEnter your account, place your bets and win!\n')

def replay():

    global play

    while True:
    
        answer = input('Would you like to continue? (y or n) \n')
        if answer.lower() == 'y':
            play = True
            return True
        elif answer.lower() == 'n':
            print("Good luck!")
            return False
        else:
           print('Wrong answer! Try again.')
           continue 

def game():

    global play

    init()

    chips = Chips(make_bet())
    
    while True:

        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        for player in (dealer_hand, player_hand):
            for i in range(2):
                player.add_card(deck.deal())
    
        take_bet(chips)

        clear_console()
        show_some(player_hand, dealer_hand)

        while play:

            hit_or_stand(deck, player_hand)

            clear_console()
            show_some(player_hand, dealer_hand)
        
            if player_hand.value > 21:
                break
        
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck, dealer_hand)
    
        clear_console()
        show_all(player_hand, dealer_hand)

        if player_hand.value > 21: player_overcards(chips)

        elif dealer_hand.value > 21: dealer_overcards(chips)

        elif dealer_hand.value > player_hand.value: dealer_win(chips)

        elif dealer_hand.value < player_hand.value: player_win(chips)

        else: tie() 
        
        print(f"On your account: {chips.total}$.")

        if replay():
            if chips.total == 0:
                print('Unfortunately, you have run out of money. '
                      '\nCome again when the money is available.')
                break
            clear_console()
            continue
        else:
            break

game()