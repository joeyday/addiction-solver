import random 

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
# If you want it shuffled, use the shuffle function
shuffled_cards = shuffle(len(cards))
shuffled_deck = [cards[i] for i in shuffled_cards]

