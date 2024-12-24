import random 
from typing import Optional

def shuffle(n: int) -> list[int]:
    numbers = list(range(n))
    shuffled = []
    while numbers:
        k = random.randint(0, len(numbers) - 1)
        shuffled.append(numbers[k])
        numbers.pop(k)
    return shuffled

def create_deck() -> list[tuple[int, str]]:
    ranks = range(1, 14)  # 1-13
    suits = ['s', 'h', 'c', 'd']
    cards = [(rank, suit) for suit in suits for rank in ranks]
    return cards

# Create and store a sorted deck
cards = create_deck()
# Shuffle the deck
shuffled_cards = shuffle(len(cards))
shuffled_deck = [cards[i] for i in shuffled_cards]

# Type alias for a card
Card = tuple[int, str]
# Type alias for the grid
Grid = list[list[Optional[Card]]]

def create_grid(rows: int, cols: int) -> Grid:
    return [[None for _ in range(cols)] for _ in range(rows)]

# Example: Create a 4x4 grid
grid = create_grid(4, 4)
# Place a card at position (0,0)
grid[0][0] = (1, 's')  # Ace of spades

