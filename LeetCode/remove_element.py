"""
Given an integer list [nums] and an integer val, remove all occurrences of val in [nums] in-place.
The order of the elements may be changed.
Then return the number of elements in [nums] which are not equal to val.

Consider the number of elements in [nums] which are not equal to val be k,
to get accepted, you need to do the following things:

Change the list [nums] such that the first k elements of [nums] contain the elements which are not equal to val.
The remaining elements of [nums] are not important as well as the size of [nums].
Return k.

>>> remove_element(nums = [3,2,2,3], val = 3)
2
"""


def remove_elements(nums: list, val: int) -> int:
    # Initialize variable to keep track of number of number of elements