import random
from enum import Enum

class Suit(Enum):
    SPADES = '♠'
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'

class Card:
    def __init__(self, suit: Suit, rank: str):
        self.suit = suit.value
        self.rank = rank

    def __str__(self):
        """
        Returns a multi-line string representation of the card.
        We use fixed width to ensure they align nicely.
        """
        # Ensure rank is formatted to take up 2 spaces (e.g., "10" vs "A ")
        r = self.rank.ljust(2) if len(self.rank) == 2 else self.rank + " "
        
        # ASCII Art construction
        line1 = "┌─────────┐"
        line2 = f"│ {r}      │" 
        line3 = f"│    {self.suit}    │"
        line4 = f"│      {r.strip().rjust(2)} │"
        line5 = "└─────────┘"
        
        return "\n".join([line1, line2, line3, line4, line5])

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        """Rebuilds a fresh deck of 52 cards."""
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        for suit in Suit:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        if not self.cards:
            return None
        return self.cards.pop()

    def __len__(self):
        return len(self.cards)

class Hand:
    def __init__(self, name="Player"):
        self.cards = []
        self.name = name

    def add_card(self, card):
        self.cards.append(card)

    def clear(self):
        self.cards = []

    @property
    def value(self):
        """
        Calculates the Blackjack value of the hand.
        Logic: Sum cards. Aces are 11 unless sum > 21, then they are 1.
        """
        val = 0
        aces = 0
        
        for card in self.cards:
            if card.rank in ['J', 'Q', 'K']:
                val += 10
            elif card.rank == 'A':
                aces += 1
                val += 11
            else:
                val += int(card.rank)
        
        # Adjust for Aces if we busted
        while val > 21 and aces > 0:
            val -= 10
            aces -= 1
            
        return val

    def __str__(self):
        """
        The TUI Logic: Stitches cards horizontally.
        """
        if not self.cards:
            return "<Empty Hand>"

        # Prepare 5 empty lines (since our card height is 5 lines)
        lines = ["", "", "", "", ""]
        
        for card in self.cards:
            card_lines = str(card).split('\n')
            for i in range(5):
                lines[i] += card_lines[i] + "  " # Add 2 spaces padding
        
        # Add the header with the hand value
        header = f"{self.name}'s Hand (Value: {self.value}):\n"
        return header + "\n".join(lines)