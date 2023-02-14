# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/14/23
# Description: This function first sorts the list of numbers, then calculates the median.

def find_median(some_nums):
    """
    Calculate the statistical median of a list of numbers.

    some_nums: a list of numbers
    Returns: The median of the list of numbers.

    The function sorts the list of numbers and then calculates the median.
    If the length of the list is even, the median is the average of the two
    middle numbers. If the length is odd, the median is the middle number.
    """

    some_nums.sort()
    length = len(some_nums)
    middle = length // 2

    if length % 2 == 0:
        return (some_nums[middle - 1] + some_nums[middle]) / 2
    else:
        return some_nums[middle]
