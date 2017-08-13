def adds_to_five(nums):
    """Returns a list of lists containing pairs of numbers that add up to 5."""

    nums_that_sum_to_5 = []
    # nums_that_sum_to_5_set = set()

    for num in range(len(nums)):
        for i, n in enumerate(nums):
            if (n + nums[num]) == 5:
                nums_that_sum_to_5.append([n, nums[num]])

    # for pair in nums_that_sum_to_5:
    #     num_pair = []
    #     for num in pair:
    #         num_pair.append(num)
    #     num_pair = set(num_pair)
    #     nums_that_sum_to_5_set.update(num_pair)

    return nums_that_sum_to_5


print adds_to_five([2, 7, 3, 4, 1, 6])
