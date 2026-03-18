#1
def count_evens(nums):
    return sum(1 for n in nums if n % 2 == 0)

#2
def big_diff(nums):
    return max(nums) - min(nums)

#3
def centered_average(nums):
    nums = sorted(nums)
    trimmed = nums[1:-1]
    return sum(trimmed) // len(trimmed)

#4
def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total

#5
def sum13(nums):
    total = 0
    i = 0
    while i < len(nums):
        if nums[i] == 13:
            i += 2
        else:
            total += nums[i]
            i += 1
    return total

#6
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

#7
def has22(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 2 and nums[i+1] == 2:
            return True
    return False

