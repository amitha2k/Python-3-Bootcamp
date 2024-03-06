import random

#Global Variables:
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return ("{} of {}".format(self.rank,self.suit))


class Deck:
    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(s,r))

    def __str__(self):
        res = ""
        for card in self.deck:
            res += Card.__str__(card) + "\n"
        return res
    
    def shuffle(self):
        random.shuffle(self.deck)
    
    def deal(self):
        return self.deck.pop(0)
    
#Tests for Deck and Cards:
# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.suit == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        big_aces = self.aces
        while big_aces > 0:
            if self.value > 21:
                self.value -= 10
                big_aces -= 1
            else:
                break

class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
        self.bet = 0

    def lose_bet(self):
        self.total -= self.bet
        self.bet = 0

#Useful Functions:
def take_bet(chips):
    while True:
        bet = input("Place a bet (you have {} chips.): ".format(chips.total))
        try:
            bet_value = int(bet)
        except:
            print("Invalid Input!")
            continue
        else:
            if chips.total < bet_value:
                print("You don't have the chips available")
                continue
            else:
                chips.bet = bet_value
                print("Bet placed!")
                break

# Tests for take_bet
# test_chips = Chips()
# take_bet(test_chips)
            
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck, hand):
    global playing
    decision = input("Would you like to Hit or Stand? (H/S): ")
    while decision not in "HS":
        print("Invalid Input!")
        decision = input("Would you like to Hit or Stand? (H/S): ")
    if decision == "H":
        return hit(deck,hand)
    else:
        print("Dealer's Turn!")
        playing = False

def show_some(player, dealer):
    print("Dealer's Hand:")
    print("**card-hidden**")
    for card in dealer.cards[1:]:
        print(card)
    print("--------------------------")
    print("Player's Hand:")
    for card in player.cards:
        print(card)   
    print("--------------------------")

def show_all(player, dealer):
    print("Dealer's Hand:")
    for card in dealer.cards:
        print(card)
    print("Dealer's total: {}".format(dealer.value))
    print("--------------------------")
    print("Player's Hand:")
    for card in player.cards:
        print(card)
    print("Player's total: {}".format(player.value))
    print("--------------------------")


def player_busts(chips):
    print("You Busted!")
    chips.lose_bet()

def player_wins(chips):
    print("You won!")
    chips.win_bet()

def dealer_busts(chips):
    print("Dealer Busted! You won!")
    chips.win_bet()

def dealer_wins(chips):
    print("Dealer wins, you lost!")
    chips.lose_bet()

def push():
    print("Push!")

# Set up the Player's chips
chips = Chips()


while True:
    # Print an opening statement
    print("Welcome to BlackJack!")

    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()

    player = Hand()
    dealer = Hand()

    for i in range(2):
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
    
    
    # Prompt the Player for their bet
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player, dealer)

    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player, dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(chips)
            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
        while dealer.value < 17:
            hit(deck, dealer)

        # Show all cards
        show_all(player, dealer)
        # Run different winning scenarios
        if dealer.value > 21:
            dealer_busts(chips)
            
        elif dealer.value > player.value:
            dealer_wins(chips)
        
        elif dealer.value < player.value:
            player_wins(chips)
        
        else:
            push()
    
    # Inform Player of their chips total 
    print("Round over!")
    print("You now have {} chips.".format(chips.total))
    # Ask to play again
    again = input("Would you like to play again? (Y/N): ")
    while again not in "YN":
        again = input("Would you like to play again? (Y/N): ")
    if again == "N":
        "Thanks For Playing!"
        break
    else:
        playing = True
        continue
    