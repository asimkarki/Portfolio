import random
from Yatzy import Yatzy

def display_dice(dice, locked):
    print("\n🎲 Your Dice:")
    for i, val in enumerate(dice):
        status = "🔒" if locked[i] else " "
        print(f"{i+1}: [{val}] {status}", end="   ")
    print()

def ask_lock(locked):
    print("\nEnter dice to toggle lock/unlock (1-5). Leave blank to keep as is.")
    user_input = input("Lock/Unlock: ").strip()
    if not user_input:
        return locked
    try:
        positions = [int(i)-1 for i in user_input.split() if 1 <= int(i) <= 5]
        for pos in positions:
            locked[pos] = not locked[pos]
    except Exception:
        print("⚠️ Invalid input. Please enter numbers 1-5.")
    return locked

def reroll_dice(game, locked):
    for i in range(5):
        if not locked[i]:
            game.dice[i] = random.randint(1, 6)

def category_menu():
    return {
        "1": ("Ones", lambda g: g.Ones()),
        "2": ("Twos", lambda g: g.Twos()),
        "3": ("Threes", lambda g: g.Threes()),
        "4": ("Fours", lambda g: g.Fours()),
        "5": ("Fives", lambda g: g.Fives()),
        "6": ("Sixes", lambda g: g.Sixes()),
        "7": ("One Pair", lambda g: g.OnePair()),
        "8": ("Two Pairs", lambda g: g.TwoPairs()),
        "9": ("Three of a Kind", lambda g: g.ThreeAlike()),
        "10": ("Four of a Kind", lambda g: g.FourAlike()),
        "11": ("Small Straight", lambda g: g.Small()),
        "12": ("Large Straight", lambda g: g.Large()),
        "13": ("Full House", lambda g: g.FullHouse()),
        "14": ("Chance", lambda g: g.Chance()),
        "15": ("Yatzy", lambda g: g.Yatzy())
    }

def choose_category(scorecard, game):
    menu = category_menu()
    print("\n📋 Available Categories:")
    for key, (name, _) in menu.items():
        if name not in scorecard:
            print(f"{key}. {name}")
    choice = input("Choose a category to score this roll: ").strip()
    while choice not in menu or menu[choice][0] in scorecard:
        choice = input("❌ Invalid or already used. Try again: ").strip()
    cat_name, func = menu[choice]
    score = func(game)
    scorecard[cat_name] = score
    print(f"✅ Scored {score} points in {cat_name}!\n")

def display_scorecard(scorecard):
    print("\n🧾 Current Scorecard:")
    total = 0
    for name in category_menu().values():
        cat_name = name[0]
        if cat_name in scorecard:
            score = scorecard[cat_name]
            print(f"{cat_name:<20} {score}")
            total += score
        else:
            print(f"{cat_name:<20} [ ]")
    print("-" * 30)
    print(f"TOTAL SCORE: {total}\n")

def play_yatzy():
    print("🎉 Welcome to YATZY!")
    print("Fill all 15 scoring categories. You get up to 3 rolls per turn.\n")

    scorecard = {}

    for round_num in range(1, 16):
        print(f"🎲 ROUND {round_num} of 15")
        game = Yatzy()
        locked = [False] * 5
        rolls = 1

        while rolls <= 3:
            display_dice(game.get_values(), locked)
            if rolls == 3:
                print("⚠️ Final roll this turn.")
                break
            locked = ask_lock(locked)
            reroll_dice(game, locked)
            rolls += 1

        display_dice(game.get_values(), locked)
        display_scorecard(scorecard)
        choose_category(scorecard, game)

    print("🎊 Game Over! Final Scorecard:")
    display_scorecard(scorecard)
    print("Thanks for playing Yatzy! 🎲")

if __name__ == "__main__":
    play_yatzy()
