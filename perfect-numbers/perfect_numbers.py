def classify(number):
    if number <= 0:
        raise ValueError("must be positive")

    sum_factors = sum([i for i in range(1, number) if number % i == 0])
    if sum_factors == number:
        return "perfect"
    return "abundant" if sum_factors > number else "deficient"
