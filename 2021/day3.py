def main():
    with open("day3.input") as f:
        numbers = [x.strip() for x in f]

    print(part1(numbers))
    print(part2(numbers))


def part1(numbers: list[str]) -> int:
    # Assume the input is all the same length.
    gamma_list = [0 for _ in numbers[0]]

    for number in numbers:
        for i in range(len(number)):
            if number[i] == "1":
                gamma_list[i] += 1

    for i, g in enumerate(gamma_list):
        n = 0
        if g > len(numbers) / 2:
            n = 1
        gamma_list[i] = n

    gamma = 0
    epsilon = 0
    for i, g in enumerate(gamma_list[::-1]):
        gamma += g << i
        epsilon += (g ^ 1) << i

    return gamma * epsilon


def part2(numbers):
    """life support rating = oxygen generator rating * CO2 scrubber rating"""
    oxy = 0
    co2 = 0

    zeroes, ones = split_numbers(numbers, 0)
    tmp_oxy = get_rating(zeroes, ones, "oxy", 0)
    tmp_co2 = get_rating(zeroes, ones, "co2", 0)

    for i in range(1, len(numbers[0])):
        zeroes, ones = split_numbers(tmp_oxy, i)
        tmp_oxy = get_rating(zeroes, ones, "oxy", i)
        if len(tmp_oxy) == 1:
            oxy = tmp_oxy[0]

        zeroes, ones = split_numbers(tmp_co2, i)
        tmp_co2 = get_rating(zeroes, ones, "co2", i)
        if len(tmp_co2) == 1:
            co2 = tmp_co2[0]

    return int(oxy, 2) * int(co2, 2)


def split_numbers(numbers: list[str], position: int) -> tuple[list[str], list[str]]:
    ones = []
    zeroes = []
    for n in numbers:
        if n[position] == "1":
            ones.append(n)
        else:
            zeroes.append(n)

    return zeroes, ones


def get_rating(
    zeroes: list[str], ones: list[str], rating_type: str, position: int
) -> list[str]:
    """bigger = oxy, smaller = co2"""

    if rating_type == "oxy":
        if len(ones) > len(zeroes):
            return ones
        if len(ones) == len(zeroes):
            return [x for x in ones + zeroes if x[position] == "1"]
        return zeroes

    else:
        if len(ones) < len(zeroes):
            return ones
        if len(ones) == len(zeroes):
            return [x for x in ones + zeroes if x[position] == "0"]
        return zeroes


if __name__ == "__main__":
    main()
