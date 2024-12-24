import random 
from typing import Optional

# Type aliases
Card = tuple[int, str]
Grid = list[list[Optional[Card]]]

def card_to_str(card: Optional[Card]) -> str:
    if card is None:
        return "   "  # Two spaces for empty spots
    rank, suit = card
    # Convert face cards to letters
    rank_str = {11: 'J', 12: 'Q', 13: 'K'}.get(rank, str(rank))
    # One space padding if single digit, no padding if double digit
    padding = " " if len(rank_str) == 1 else ""
    return f"{padding}{rank_str}{suit}"

def create_deck() -> list[Card]:
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

def create_grid(rows: int, cols: int) -> Grid:
    return [[None for _ in range(cols)] for _ in range(rows)]

# Create and store a shuffled deck
deck = shuffle(create_deck())

# Example: Create a 13×4 grid
grid = create_grid(4, 13)

# Place cards from the shuffled deck onto the grid, from left
# to right and top to bottom, replacing Aces with None
for r in range(len(grid)):
    for c in range(len(grid[r])):
        card = deck.pop(0)
        if card[0] == 1:
            grid[r][c] = None
        else:
            grid[r][c] = card

for row in grid:
    print(' '.join(card_to_str(card) for card in row))