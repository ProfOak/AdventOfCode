"""
Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the
IDs of those games?
"""
import collections

# The Elf would first like to know which games would have been possible if the
# bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?
max_cubes = {"red": 12, "green": 13, "blue": 14}


Game = dict[str, int]


def is_possible(game: Game) -> bool:
    for color, max_value in max_cubes.items():
        if max_value < game.get(color, 0):
            return False
    return True


def process_games(line: str) -> tuple[Game, int]:
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    game = collections.defaultdict(int)
    game_info, line = line.split(":", 1)
    _, number = game_info.split(" ", 1)
    number = int(number)
    max_count = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    possible = number

    for colors in line.split(";"):
        game = {}
        for color in colors.split(", "):
            count, color = color.strip().split(" ")
            game[color] = int(count)
            max_count[color] = max(max_count[color], int(count))
            if not is_possible(game):
                possible = 0

    power = max_count["red"] * max_count["blue"] * max_count["green"]
    return number, power


total_one = 0
total_two = 0
with open("day2.input") as f:
    for line in f:
        one, two = process_games(line)
        total_one += one
        total_two += two

print(total_one)
print(total_two)
