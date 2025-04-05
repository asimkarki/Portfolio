import pytest
from Yatzy import Yatzy

class MockDie:
    def __init__(self, value):
        self.value = value
        self.locked = False

    def roll(self):
        return self.value


def create_yatzy_with_values(values):
    y = Yatzy()
    y.dice = [MockDie(v) for v in values]
    return y

# Test number scoring methods
def test_ones():
    y = create_yatzy_with_values([1, 1, 2, 4, 6])
    assert y.Ones() == 2

def test_twos():
    y = create_yatzy_with_values([2, 2, 2, 3, 5])
    assert y.Twos() == 6

def test_threes():
    y = create_yatzy_with_values([3, 3, 1, 5, 6])
    assert y.Threes() == 6

def test_fours():
    y = create_yatzy_with_values([4, 4, 4, 4, 4])
    assert y.Fours() == 20

def test_fives():
    y = create_yatzy_with_values([1, 2, 5, 5, 5])
    assert y.Fives() == 15

def test_sixes():
    y = create_yatzy_with_values([6, 6, 6, 6, 6])
    assert y.Sixes() == 30

# Test One Pair
def test_one_pair():
    y = create_yatzy_with_values([1, 2, 2, 3, 4])
    assert y.OnePair() == 4

def test_one_pair_no_pair():
    y = create_yatzy_with_values([1, 2, 3, 4, 5])
    assert y.OnePair() == 0

# Test Two Pairs
def test_two_pairs():
    y = create_yatzy_with_values([3, 3, 5, 5, 1])
    assert y.TwoPairs() == 16

def test_two_pairs_only_one_pair():
    y = create_yatzy_with_values([3, 3, 2, 6, 5])
    assert y.TwoPairs() == 0

# Test Three of a Kind
def test_three_alike():
    y = create_yatzy_with_values([4, 4, 4, 2, 1])
    assert y.ThreeAlike() == 12

def test_three_alike_none():
    y = create_yatzy_with_values([1, 2, 3, 4, 5])
    assert y.ThreeAlike() == 0

# Test Four of a Kind
def test_four_alike():
    y = create_yatzy_with_values([6, 6, 6, 6, 1])
    assert y.FourAlike() == 24

def test_four_alike_none():
    y = create_yatzy_with_values([2, 2, 2, 3, 3])
    assert y.FourAlike() == 0

# Test Small Straight
def test_small_straight():
    y = create_yatzy_with_values([1, 2, 3, 4, 5])
    assert y.Small() == 15

def test_small_straight_wrong_order():
    y = create_yatzy_with_values([5, 4, 3, 2, 1])
    assert y.Small() == 15

def test_small_straight_fail():
    y = create_yatzy_with_values([1, 2, 3, 5, 6])
    assert y.Small() == 0

# Test Large Straight
def test_large_straight():
    y = create_yatzy_with_values([2, 3, 4, 5, 6])
    assert y.Large() == 20

def test_large_straight_fail():
    y = create_yatzy_with_values([1, 2, 3, 4, 6])
    assert y.Large() == 0

# Test Full House
def test_full_house():
    y = create_yatzy_with_values([2, 2, 3, 3, 3])
    assert y.FullHouse() == 13

def test_full_house_wrong_counts():
    y = create_yatzy_with_values([2, 2, 2, 2, 3])
    assert y.FullHouse() == 0

def test_full_house_fail():
    y = create_yatzy_with_values([1, 1, 2, 3, 4])
    assert y.FullHouse() == 0

# Test Chance
def test_chance():
    y = create_yatzy_with_values([6, 5, 4, 3, 2])
    assert y.Chance() == 20

# Test Yatzy
def test_yatzy_success():
    y = create_yatzy_with_values([5, 5, 5, 5, 5])
    assert y.Yatzy() == 50

def test_yatzy_fail():
    y = create_yatzy_with_values([5, 5, 5, 5, 4])
    assert y.Yatzy() == 0
