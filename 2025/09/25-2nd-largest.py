'''
Given an array, return the second largest distinct number.
'''

def second_largest(arr):
    largest_num = arr[0]
    second_largest_num = arr[0]

    for a in arr:
        if a > largest_num:
            second_largest_num = largest_num
            largest_num = a
        elif a != largest_num and a > second_largest_num:
            second_largest_num = a
        elif a != largest_num and largest_num == second_largest_num:
            second_largest_num = a

    return second_largest_num

print("Success") if second_largest([1, 2, 3, 4]) == 3 else print("Failed")
print("Success") if second_largest([20, 139, 94, 67, 31]) == 94 else print("Failed")
print("Success") if second_largest([2, 3, 4, 6, 6]) == 4 else print("Failed")
print("Success") if second_largest([10, -17, 55.5, 44, 91, 0]) == 55.5 else print("Failed")
print("Success") if second_largest([1, 0, -1, 0, 1, 0, -1, 1, 0]) == 0 else print("Failed")