totals = [0]

with open("day1.input") as f:
    for line in f:
        line = line.strip()
        if not line:
            totals.append(0)
        else:
            totals[-1] += int(line)

top3 = sorted(totals)[-3:]
print(top3)
print(sum(top3))
