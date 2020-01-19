def find3numbers(input, target):
    input_len = len(input)
    for i in range(0, input_len - 2):
        for j in range(i + 1, input_len - 1):
            for k in range(j + 1, input_len):
                if input[i] + input[j] + input[k] == target:
                    print(input[i], input[j], input[k])


find3numbers([1, 4, 45, 6, 10, 8], 22)

# Trying with hash based with


def findTriplets(input, sum):
    input_len = len(input)
    for i in range(0, input_len - 1):
        temp_set = set()
        current_sum = sum - input[i]
        for j in range(i + 1, input_len):
            if (current_sum - input[j]) in temp_set:
                print(f"Triplet is {input[i]}, {input[j]}, {current_sum - input[j]}")
            temp_set.add(input[j])


findTriplets([1, 4, 45, 6, 10, 8], 22)

