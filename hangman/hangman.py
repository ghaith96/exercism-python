# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"

MASK = "_"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.guessed_letters = list()

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("already did 9 guesses")

        if char in self.word and char not in self.guessed_letters:
            self.guessed_letters.append(char)
        else:
            self.remaining_guesses -= 1
        self.update_game_status()

    def update_game_status(self):
        if MASK not in self.get_masked_word():
            self.status = STATUS_WIN

        if self.remaining_guesses < 0:
            self.status = STATUS_LOSE

    def get_masked_word(self):
        return "".join(
            [char if char in self.guessed_letters else MASK for char in self.word]
        )

    def get_status(self):
        return self.status
