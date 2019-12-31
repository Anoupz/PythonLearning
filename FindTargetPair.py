"""
Find the target pair for in the given list
"""


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
