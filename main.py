import random 
from typing import Optional

# Type aliases
Card = tuple[int, str]
Grid = list[list[Optional[Card]]]

def create_deck() -> list[tuple[int, str]]:
    ranks = range(1, 14)  # 1-13
    suits = ['s', 'h', 'c', 'd']
    cards = [(rank, suit) for suit in suits for rank in ranks]
    return cards

def shuffle(array: list) -> list:
    result = array.copy()
    for i in range(len(result)-1, 0, -1):
        j = random.randint(0, i)
        result[i], result[j] = result[j], result[i]
    return result

# Create and store a sorted deck
deck = create_deck()
# Shuffle the deck
shuffled_deck = shuffle(deck)


def create_grid(rows: int, cols: int) -> Grid:
    return [[None for _ in range(cols)] for _ in range(rows)]

# Example: Create a 4x4 grid
grid = create_grid(4, 4)
# Place a card at position (0,0)
grid[0][0] = (1, 's')  # Ace of spades

