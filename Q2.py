"""
Your task is ultimately to implement a function that takes in an array and a integer.
You want to return the *LENGTH* of the shortest subarray whose sum 
is at least the integer,
and -1 if no such sum exists.
"""

def sub_array_exceeds_sum(arr, target):
    lengthlist = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr) + 1):
            sub_array = arr[i:j]
            # print(sum(sub_array))
            if sum(sub_array) >= target:
                # print(sub_array)
                lengthlist.append(len(sub_array))
    # print(lengthlist)
    print(min(lengthlist))

    # for i in range(len:
    #     for j in range(i,len(arr)):
    #         sub_array = arr[i:j]
    #         print(sub_array)

    # print(sub_array)

sub_array_exceeds_sum([1, 2, 3, 4], 5)


# if __name__ == '__main__':
# from mark import mark

# test_cases = [
# ( ([1, 2, 3, 4], 6), 2 ),
# ( ([1, 2, 3, 4], 12),  -1 ),
# ( ([1, 2, 3, 4], 10), 4 ),
# ( ([1, 2, 3, 4], 4), 1 ),
# ( ([], 1), -1 ),
# ( ([], 0), 0 ),
# ]

