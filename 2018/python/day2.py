"""This was a little gross. There's probably a better way to do this"""

with open('../inputs/day2.txt') as f:
    boxes = [n for n in f if n.strip()]


def part1_helper(box):
    boxmap, two, three = {}, 0, 0
    for char in box:
        if not boxmap.get(char):
            boxmap[char] = 0
        boxmap[char] += 1

    for key, value in boxmap.items():
        if value == 2:
            two = 1
        elif value == 3:
            three = 1

    return two, three


def part1(boxes):
    two, three = 0, 0
    for box in boxes:
        temp2, temp3 = part1_helper(box)
        two += temp2
        three += temp3

    return two * three


def part2(boxes):
    for box1 in boxes:
        for box2 in boxes:
            if [a == b for a, b in zip(box1, box2)].count(False) == 1:
                return ''.join([a for a, b in zip(box1, box2) if a == b])


print(part1(boxes))
print(part2(boxes))
