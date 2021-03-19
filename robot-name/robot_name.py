from string import ascii_uppercase, digits
import random


def get_random_name() -> str:
    random.seed(random.seed(random.choice(ascii_uppercase)))
    name = "".join([*random.sample(ascii_uppercase, 2), *random.sample(digits, 3)])
    return f"{name}"


class Robot:
    def __init__(self):
        self.reset()

    def reset(self):
        self.name = get_random_name()
