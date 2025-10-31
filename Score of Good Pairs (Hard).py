def findScoreSum(nums):
    count = {}
    sum_idx = {}
    total = 0
    n = len(nums)

    for j in range(n):
        val = nums[j]
        if val in count:
            total += j * count[val] - sum_idx[val]
            count[val] += 1
            sum_idx[val] += j
        else:
            count[val] = 1
            sum_idx[val] = j
    return total
