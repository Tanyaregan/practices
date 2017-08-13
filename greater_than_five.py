def adds_to_five(nums):
    """Returns a list of lists containing pairs of numbers that add up to 5."""

    nums_that_sum_to_5 = []
    summed = []
    index = 0

    for num in nums:
        for n in nums:
            if n + nums[index] == 5:
                summed.append(n)
                summed.append(nums[index])
                nums_that_sum_to_5.append(summed)
                index += 1

    return nums_that_sum_to_5

print adds_to_five([2, 7, 3, 4, 1, 6])

#[2,3], [4,1]]
