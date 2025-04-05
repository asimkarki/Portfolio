import random

class Die:
    def __init__(self):
        self.value = random.randint(1, 6)
        self.locked = False

    def roll(self):
        if not self.locked:
            self.value = random.randint(1, 6)
        return self.value

    def lock(self):
        self.locked = True

    def unlock(self):
        self.locked = False