with open('../inputs/day1.txt') as f:
    numbers = [int(n) for n in f if n.strip()]


def part1(numbers):
    return sum(numbers)


def part2(numbers):
    """
    If code challenges have taught me anything, it's that hashmaps are
    always the answer.
    """
    nummap, i, total = {}, 0, 0
    while True:
        total += numbers[i]
        if nummap.get(total):
            return total

        nummap[total] = True
        i = (i + 1) % len(numbers)


print(part1(numbers))
print(part2(numbers))
