import random 

def shuffle(n: int) -> list[int]:
    numbers = list(range(n))
    shuffled = []
    while numbers:
        k = random.randint(0, len(numbers) - 1)
        shuffled.append(numbers[k])
        numbers.pop(k)
    return shuffled



cards = []

