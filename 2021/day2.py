from typing import NamedTuple


def main():
    with open("day2.input") as f:
        commands = []
        for line in f:
            direction, n = line.split(" ")
            commands.append(Command(direction, int(n)))

    print(part1(commands))
    print(part2(commands))


class Command(NamedTuple):
    direction: str
    distance: int


def part1(commands: list[Command]) -> int:
    x, y = 0, 0
    for c in commands:
        if c.direction == "forward":
            x += c.distance
        if c.direction == "up":
            y -= c.distance
        if c.direction == "down":
            y += c.distance
    return x * y


def part2(commands: list[Command]) -> int:
    x, y, aim = 0, 0, 0
    for c in commands:
        if c.direction == "forward":
            x += c.distance
            y += c.distance * aim
        if c.direction == "up":
            aim -= c.distance
        if c.direction == "down":
            aim += c.distance
    return x * y


if __name__ == "__main__":
    main()
