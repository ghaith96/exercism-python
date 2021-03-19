ALPHABET_COUNT = 26


def is_pangram(sentence):
    if len(sentence) < ALPHABET_COUNT:
        return False

    sentence = sentence.lower()
    seen_letters = {}
    for alpha_letter in filter(lambda letter: letter.isalpha(), sentence):
        seen_letters[alpha_letter] = True

    if len(seen_letters) < ALPHABET_COUNT:
        return False

    return True
