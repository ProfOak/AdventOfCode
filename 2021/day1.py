def main():
    with open("day1.input") as f:
        numbers = list(map(int, f))

    print(part1(numbers))
    print(part2(numbers))


def part1(numbers):
    total = 0
    prev = numbers[0]
    for next_n in numbers[1:]:
        if next_n > prev:
            total += 1

        prev = next_n

    return total


def part2(numbers):
    total = 0
    prev = numbers[0] + numbers[1] + numbers[2]

    for i in range(len(numbers[1:])):
        if i + 3 > len(numbers):
            break

        next_n = numbers[i] + numbers[i + 1] + numbers[i + 2]
        if next_n > prev:
            total += 1

        prev = next_n
    return total


if __name__ == "__main__":
    main()
