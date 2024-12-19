from collections import Counter

with open("day1.input") as f:
    left, right = zip(*(map(int, line.strip().split("   ")) for line in f), strict=True)

left = sorted(left)
right = sorted(right)
print(sum(abs(l - r) for l, r in zip(left, right)))

# part 2
right = Counter(right)
print(sum(l * right[l] for l in left))
