'''
Given an array of integers from 1 to n, inclusive, return an array of all the missing integers between 1 and n (where n is the largest number in the given array).
 - The given array may be unsorted and may contain duplicates.
 - The returned array should be in ascending order.
 - If no integers are missing, return an empty array.

'''

def find_missing_numbers(arr):
    sorted_arr = sorted(set(arr))
    missing_numbers_arr = []

    ind = 0
    while ind < len(sorted_arr):
        try:
            num_1 = sorted_arr[ind]
            num_2 = sorted_arr[ind + 1]

            dif = num_2 - num_1

            if dif > 0:
                missing_number = num_1 + 1
                while missing_number < num_2:
                    missing_numbers_arr.append(missing_number)
                    missing_number += 1

        except:
            pass

        ind += 1

    return missing_numbers_arr

print("Success") if find_missing_numbers([1, 3, 5]) == [2, 4] else print("Failed")
print("Success") if find_missing_numbers([1, 2, 3, 4, 5]) == [] else print("Failed")
print("Success") if find_missing_numbers([1, 10]) == [2, 3, 4, 5, 6, 7, 8, 9] else print("Failed")
print("Success") if find_missing_numbers([10, 1, 10, 1, 10, 1]) == [2, 3, 4, 5, 6, 7, 8, 9] else print("Failed")
print("Success") if find_missing_numbers([3, 1, 4, 1, 5, 9]) == [2, 6, 7, 8] else print("Failed")
print("Success") if find_missing_numbers([1, 2, 3, 4, 5, 7, 8, 9, 10, 12, 6, 8, 9, 3, 2, 10, 7, 4]) == [11] else print("Failed")