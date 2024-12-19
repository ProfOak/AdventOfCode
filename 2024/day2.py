with open("day2.input") as f:
    lines = [x.strip() for x in f]


def normalize(nums: list[int]) -> list[int]:
    if nums[0] < nums[1]:
        nums = nums[::-1]
    return nums


def is_safe2(nums: list[int]) -> bool:
    dampened = False
    diffs1 = (0 < nums[i] - nums[i + 1] < 4 for i in range(len(nums) - 1))
    diffs2 = [0 < nums[i] - nums[i + 2] < 4 for i in range(len(nums) - 2)]
    for d1, d2 in zip(diffs1, diffs2, strict=False):
        if not d1:
            if dampened:
                return False
            if not d2:
                return False
            dampened = True

    return True


def is_safe1(nums: list[int]) -> bool:
    return all(0 < nums[i] - nums[i + 1] < 4 for i in range(len(nums) - 1))


print(sum(1 for line in lines if is_safe1(normalize(list(map(int, line.split(" ")))))))

print(sum(1 for line in lines if is_safe2(normalize(list(map(int, line.split(" ")))))))
