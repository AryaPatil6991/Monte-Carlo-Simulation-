# main.py
from blackjack import BlackjackGame

def main():
    print("Welcome to Modular Python Blackjack!")
    
    # Initialize the engine once (creates the deck)
    game = BlackjackGame()
    
    playing = True
    while playing:
        winner = game.play_round()
        print(f"*** Result: {winner} Wins! ***")
        
        # Input validation for replay
        while True:
            again = input("\nPlay again? (y/n): ").lower()
            if again in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'.")
            
        if again == 'n':
            print("Thanks for playing!")
            playing = False

if __name__ == "__main__":
    main()