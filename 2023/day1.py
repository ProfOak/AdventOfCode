number_list = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def find_number(line: str, include_strings: bool = False) -> int:
    """Return the first and last number that appears on a line as one number."""
    numbers: list[int] = []

    for i, s in enumerate(line):
        if s.isdigit():
            numbers.append(int(s))
            continue

        if include_strings:
            for number_index, number in enumerate(number_list):
                if line[i:].startswith(number):
                    numbers.append(number_index)
                    break

    return (numbers[0] * 10) + numbers[-1]


part_one = 0
part_two = 0
with open("day1.input") as f:
    for line in f:
        part_one += find_number(line)
        part_two += find_number(line, include_strings=True)

print(part_one)
print(part_two)
