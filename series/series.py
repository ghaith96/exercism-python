def slices(series, length):
    if not series:
        raise ValueError("invalid series")
    if length <= 0:
        raise ValueError("Length must be positive integer")
    if length > len(series):
        raise ValueError("Length must be less or equal to series length")
    return [
        series[start : start + length] for start in range(0, len(series) - length + 1)
    ]
