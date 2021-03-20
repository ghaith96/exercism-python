from random import randint
from math import floor


class Character:
    def __init__(self):
        self.strength = generate_score()
        self.dexterity = generate_score()
        self.constitution = generate_score()
        self.intelligence = generate_score()
        self.wisdom = generate_score()
        self.charisma = generate_score()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        return generate_score()


def generate_score():
    scores = [randint(1, 6) for _ in range(7)]
    return sum(sorted(scores)[:4])


def modifier(constitution):
    return floor((constitution - 10) / 2)