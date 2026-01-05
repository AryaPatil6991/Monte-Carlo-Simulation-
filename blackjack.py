import time
from cards import Deck, Hand

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand("Player")
        self.dealer_hand = Hand("Dealer")

    def deal_initial(self):
        self.player_hand.clear()
        self.dealer_hand.clear()
        if len(self.deck) < 15:
            print("\n--- Reshuffling Deck ---")
            self.deck.reset()
        for _ in range(2):
            self.player_hand.add_card(self.deck.draw())
            self.dealer_hand.add_card(self.deck.draw())

    def print_table(self, reveal_dealer=False):
        print("\n" + "="*50)
        if reveal_dealer:
            print(self.dealer_hand)
        else:
            print(f"Dealer's Hand (Value: ?):")
            # Assumes 5-line card height
            print("┌─────────┐  ┌─────────┐") 
            print("│░░░░░░░░░│  " + str(self.dealer_hand.cards[1]).split('\n')[1])
            print("│░░░░░░░░░│  " + str(self.dealer_hand.cards[1]).split('\n')[2])
            print("│░░░░░░░░░│  " + str(self.dealer_hand.cards[1]).split('\n')[3])
            print("└─────────┘  └─────────┘")
        print("-" * 50)
        print(self.player_hand)
        print("="*50 + "\n")

    def play_round(self):
        self.deal_initial()
        
        # Player Turn
        while True:
            self.print_table(reveal_dealer=False)
            if self.player_hand.value == 21:
                print("Blackjack! You have 21.")
                break
            if self.player_hand.value > 21:
                print("Bust! You went over 21.")
                return "Dealer" 

            move = input("Action: [H]it or [S]tand? > ").lower()
            if move == 'h':
                new_card = self.deck.draw()
                print(f"Drawing... {new_card.rank} of {new_card.suit}")
                self.player_hand.add_card(new_card)
                time.sleep(0.5)
            elif move == 's':
                break
            else:
                print("Invalid input.")

        # Dealer Turn
        print("\n--- Dealer's Turn ---")
        self.print_table(reveal_dealer=True)
        time.sleep(1)

        while self.dealer_hand.value < 17:
            print("Dealer hits...")
            time.sleep(1)
            self.dealer_hand.add_card(self.deck.draw())
            self.print_table(reveal_dealer=True)
            if self.dealer_hand.value > 21:
                print("Dealer Busts!")
                return "Player"

        # Result
        p_val = self.player_hand.value
        d_val = self.dealer_hand.value
        print(f"Final Score -> Player: {p_val} | Dealer: {d_val}")
        
        if p_val > d_val: return "Player"
        elif d_val > p_val: return "Dealer"
        else: return "Push"