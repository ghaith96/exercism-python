"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


def get_result_freq(dice):
    return {die: dice.count(die) for die in set(dice)}


def simple_sum(dice, desired_num):
    return sum([die for die in dice if die == desired_num])


def full_house_sum(dice):
    freq = get_result_freq(dice)
    filtered_dice = [die for die in dice if freq[die] == 2 or freq[die] == 3]
    return sum(dice) if len(filtered_dice) == 5 else 0


def four_of_a_kind_computer(dice):
    freq = get_result_freq(dice)
    filtered_list = [die for die in dice if freq[die] >= 4]
    return sum(filtered_list[:4])


def little_straight_sum(dice):
    for idx, die in enumerate(sorted(dice)):
        if idx + 1 != die:
            return 0
    return 30


def big_straight_sum(dice):
    for idx, die in enumerate(sorted(dice)):
        if idx + 2 != die:
            return 0
    return 30


def choise_sum(dice):
    return sum(dice)


def yacht_sum(dice):
    return 50 if len(set(dice)) == 1 else 0


# Score categories.
# Change the values as you see fit.
YACHT = "YACHT"
ONES = "ONES"
TWOS = "TWOS"
THREES = "THREES"
FOURS = "FOURS"
FIVES = "FIVES"
SIXES = "SIXES"
FULL_HOUSE = "FULL_HOUSE"
FOUR_OF_A_KIND = "FOUR_OF_A_KIND"
LITTLE_STRAIGHT = "LITTLE_STRAIGHT"
BIG_STRAIGHT = "BIG_STRAIGHT"
CHOICE = "CHOICE"

computers = dict(
    ONES=lambda dice: simple_sum(dice, 1),
    TWOS=lambda dice: simple_sum(dice, 2),
    THREES=lambda dice: simple_sum(dice, 3),
    FOURS=lambda dice: simple_sum(dice, 4),
    FIVES=lambda dice: simple_sum(dice, 5),
    SIXES=lambda dice: simple_sum(dice, 6),
    YACHT=yacht_sum,
    FULL_HOUSE=full_house_sum,
    FOUR_OF_A_KIND=four_of_a_kind_computer,
    LITTLE_STRAIGHT=little_straight_sum,
    BIG_STRAIGHT=big_straight_sum,
    CHOICE=choise_sum,
)


def score(dice, category):
    return computers[category](dice)
