def remove_duplicates(nums):
    if len(nums) == 0:
        return 0

    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1

    return k


print(remove_duplicates([1, 4, 1, 5, 6, 9, 4, 5]))
