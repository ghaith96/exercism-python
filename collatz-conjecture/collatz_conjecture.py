def steps(n):
    if n <= 0:
        raise ValueError("Positive numbers only pls.")
    steps = 0
    while n != 1:
        n = n / 2 if n % 2 == 0 else (3 * n) + 1
        steps += 1
    return steps
