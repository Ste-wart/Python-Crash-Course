"""Die by Stewart Magnus"""

from random import randint
from collections import Counter


class Die:
    """A Class representing a single die."""

    __slots__ = ['sides', 'size']

    def __init__(self, sides: int = 6) -> None:
        """Using a six-sided die"""
        self.sides = sides
        self.size = list(range(1, self.sides + 1))

    def __repr__(self) -> str:
        return f'A {self.sides} sided Die'

    def __len__(self) -> int:
        return self.sides

    def roll(self) -> int:
        """Return a random value between 1 and number of sides."""
        return randint(1, self.sides)

    def simulation(self, n: int = 1000) -> list[int]:
        """n number of die or dice throws."""
        return [self.roll() for _ in range(n)]

    @classmethod
    def frequency(cls, sims: list[int]) -> Counter:
        """Number of occurrences for each on the die side or sum of sides for dice."""
        return Counter(sims)

    @classmethod
    def dice(cls, *die) -> list[int] | str:
        if len(die) > 1:
            return [sum(values) for values in zip(*die)]
        else:
            print('For a Die use @simulation method.')


d = Die()  # An instance.
print(d)

# Make some rolls, and store results in a list.
s1 = d.simulation(100)
s2 = d.simulation(100)
s3 = d.simulation(100)

results = Die.dice(s1, s2, s3)
print(len(results))
print(results)

# Analyze the results.
freq = d.frequency(results)
print(freq)
