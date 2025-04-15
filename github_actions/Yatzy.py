import random

class Yatzy:
    def __init__(self):
        self.dice = []
        self.roll()

    def roll(self):
        self.dice = [random.randint(1, 6) for _ in range(5)]

    def get_values(self):
        return self.dice

    def count(self, num):
        return self.dice.count(num) * num

    def Ones(self): return self.count(1)
    def Twos(self): return self.count(2)
    def Threes(self): return self.count(3)
    def Fours(self): return self.count(4)
    def Fives(self): return self.count(5)
    def Sixes(self): return self.count(6)

    def OnePair(self):
        for val in sorted(set(self.dice), reverse=True):
            if self.dice.count(val) >= 2:
                return val * 2
        return 0

    def TwoPairs(self): #
        values = sorted(self.get_values(), reverse=True)
        pairs = []
        counted = set()
        for val in values:
            if values.count(val) >= 2 and val not in counted:
                pairs.append(val)
                counted.add(val)
            if len(pairs) == 2:
                break
        if len(pairs) == 2:
            return sum(p * 2 for p in pairs)
        return 0


    def ThreeAlike(self):
        for val in set(self.dice):
            if self.dice.count(val) >= 3:
                return val * 3
        return 0

    def FourAlike(self):
        for val in set(self.dice):
            if self.dice.count(val) >= 4:
                return val * 4
        return 0

    def Small(self):
        return 15 if sorted(self.dice) == [1, 2, 3, 4, 5] else 0

    def Large(self):
        return 20 if sorted(self.dice) == [2, 3, 4, 5, 6] else 0

    def FullHouse(self):
        unique = set(self.dice)
        if len(unique) == 2:
            counts = [self.dice.count(val) for val in unique]
            if sorted(counts) == [2, 3]:
                return sum(self.dice)
        return 0

    def Chance(self):
        return sum(self.dice)

    def Yatzy(self):
        return 50 if len(set(self.dice)) == 1 else 0