import random
from Die import Die
class Yatzy:
    def __init__(self):
        self.dice = [Die() for _ in range(5)]
        self.roll()

    def roll(self):
        for die in self.dice:
            die.roll()

    def get_values(self):
        return [die.value for die in self.dice]

    def count(self, num):
        return self.get_values().count(num) * num

    def Ones(self): return self.count(1)
    def Twos(self): return self.count(2)
    def Threes(self): return self.count(3)
    def Fours(self): return self.count(4)
    def Fives(self): return self.count(5)
    def Sixes(self): return self.count(6)

    def OnePair(self):
        values = sorted(self.get_values(), reverse=True)
        for val in set(values):
            if values.count(val) >= 2:
                return val * 2
        return 0

    def TwoPairs(self):
        values = sorted(self.get_values(), reverse=True)
        pairs = []
        for val in set(values):
            if values.count(val) >= 2:
                pairs.append(val)
        if len(pairs) >= 2:
            return sum(pair * 2 for pair in pairs[:2])
        return 0

    def ThreeAlike(self):
        for val in set(self.get_values()):
            if self.get_values().count(val) >= 3:
                return val * 3
        return 0

    def FourAlike(self):
        for val in set(self.get_values()):
            if self.get_values().count(val) >= 4:
                return val * 4
        return 0

    def Small(self):
        return 15 if sorted(self.get_values()) == [1, 2, 3, 4, 5] else 0

    def Large(self):
        return 20 if sorted(self.get_values()) == [2, 3, 4, 5, 6] else 0

    def FullHouse(self):
        vals = self.get_values()
        unique = set(vals)
        if len(unique) == 2:
            first, second = unique
            if vals.count(first) in [2, 3] and vals.count(second) in [2, 3]:
                return sum(vals)
        return 0

    def Chance(self):
        return sum(self.get_values())

    def Yatzy(self):
        return 50 if len(set(self.get_values())) == 1 else 0