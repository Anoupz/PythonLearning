"""
Find the target pair for in the given list
"""

from typing import List


def find_target_pair(input_list, target):
    result_dic: dict = {}
    target_found = False
    for value in input_list:
        result = target - value
        if result_dic.get(result):
            print(f"Yes found it and the pair is {result} - {value}")
            target_found = True
            break
        else:
            result_dic[value] = result
    if not target_found:
        print(f"Sorry we didn't find any pair for target {target}")


find_target_pair(input_list=[2, 5, 5, 3, 7, 9], target=16)


"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    result_dict = {}
    for idx, num in enumerate(nums):
        result = target - num
        if result in result_dict:
            result_idx = nums.index(result)
            return [idx, result_idx]
            break
        else:
            result_dict[num] = result


print(twoSum([2, 7, 11, 15], 9))
