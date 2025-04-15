from Yatzy import Yatzy

def test_get_values():
    game = Yatzy()
    game.dice = [1, 2, 3, 4, 5]
    assert game.get_values() == [1, 2, 3, 4, 5]
    print("✅ Test for get_values passed")

def test_count():
    game = Yatzy()
    game.dice = [1, 1, 2, 3, 4]
    assert game.count(1) == 2
    assert game.count(2) == 2
    assert game.count(6) == 0
    print("✅ Test for count passed")

def test_upper_section():
    game = Yatzy()
    game.dice = [1, 1, 2, 2, 6]
    assert game.Ones() == 2
    assert game.Twos() == 4
    assert game.Threes() == 0
    assert game.Fours() == 0
    assert game.Fives() == 0
    assert game.Sixes() == 6
    print("✅ Test for upper section methods passed")

def test_one_pair():
    game = Yatzy()
    game.dice = [3, 3, 4, 5, 6]
    assert game.OnePair() == 6
    game.dice = [1, 2, 3, 4, 5]
    assert game.OnePair() == 0
    print("✅ Test for OnePair passed")

def test_two_pairs():
    game = Yatzy()
    game.dice = [3, 3, 4, 4, 6]
    assert game.TwoPairs() == 14
    game.dice = [2, 2, 2, 5, 6]
    assert game.TwoPairs() == 0
    print("✅ Test for TwoPairs passed")

def test_three_alike():
    game = Yatzy()
    game.dice = [2, 2, 2, 3, 4]
    assert game.ThreeAlike() == 6
    game.dice = [1, 1, 2, 2, 3]
    assert game.ThreeAlike() == 0
    print("✅ Test for ThreeAlike passed")

def test_four_alike():
    game = Yatzy()
    game.dice = [5, 5, 5, 5, 2]
    assert game.FourAlike() == 20
    game.dice = [3, 3, 3, 2, 2]
    assert game.FourAlike() == 0
    print("✅ Test for FourAlike passed")

def test_small_straight():
    game = Yatzy()
    game.dice = [1, 2, 3, 4, 5]
    assert game.Small() == 15
    game.dice = [2, 3, 4, 5, 6]
    assert game.Small() == 0
    print("✅ Test for Small passed")

def test_large_straight():
    game = Yatzy()
    game.dice = [2, 3, 4, 5, 6]
    assert game.Large() == 20
    game.dice = [1, 2, 3, 4, 5]
    assert game.Large() == 0
    print("✅ Test for Large passed")

def test_full_house():
    game = Yatzy()
    game.dice = [2, 2, 3, 3, 3]
    assert game.FullHouse() == 13
    game.dice = [2, 2, 2, 2, 2]
    assert game.FullHouse() == 0
    game.dice = [2, 2, 2, 3, 4]
    assert game.FullHouse() == 0
    print("✅ Test for FullHouse passed")

def test_chance():
    game = Yatzy()
    game.dice = [1, 2, 3, 4, 5]
    assert game.Chance() == 15
    print("✅ Test for Chance passed")

def test_yatzy():
    game = Yatzy()
    game.dice = [6, 6, 6, 6, 6]
    assert game.Yatzy() == 50
    game.dice = [6, 6, 6, 6, 5]
    assert game.Yatzy() == 0
    print("✅ Test for Yatzy passed")


if __name__ == "__main__":
    test_get_values()
    test_count()
    test_upper_section()
    test_one_pair()
    test_two_pairs()
    test_three_alike()
    test_four_alike()
    test_small_straight()
    test_large_straight()
    test_full_house()
    test_chance()
    test_yatzy()
    print("\n🎉 All tests passed successfully!")
