def calculate_mean(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

assert 10.0 == calculate_mean([0, 10, 20])
assert 1.0 == calculate_mean([1000, 3500, 7_000_000])
