import re

with open("day3.input") as f:
    matches = re.findall(r"(mul\(\d+,\d+\)|do\(\)|don't\(\))", f.read().strip())


op_pattern = re.compile(r"(mul)\((\d+),(\d+)\)")
operations = {
    "mul": lambda a, b: a * b,
}


def calculate(text: str) -> int:
    match = op_pattern.fullmatch(text)
    if not match and len(match.groups()) != 3:
        raise Exception("uh oh")
    op, a, b = match.groups()
    return operations[op](int(a), int(b))


print(sum(calculate(match) for match in matches if match not in ("do()", "don't()")))

trimmed = []
enable = True
for match in matches:
    if match == "don't()":
        enable = False
    elif match == "do()":
        enable = True
    elif enable:
        trimmed.append(match)


print(sum(calculate(match) for match in trimmed))
