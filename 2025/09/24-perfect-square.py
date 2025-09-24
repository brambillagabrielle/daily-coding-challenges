'''
Given an integer, determine if it is a perfect square.
 - A number is a perfect square if you can multiply an integer by itself to achieve the number. For example, 9 is a perfect square because you can multiply 3 by itself to get it.
'''

def is_perfect_square(n):
    if n < 0:
        return False
    elif n <= 1:
        return True
    else:
        for i in range(1, int(n / 2)):
            if (i * i) == n:
                return True

    return False

print("Success") if is_perfect_square(9) == True else print("Failed")
print("Success") if is_perfect_square(49) == True else print("Failed")
print("Success") if is_perfect_square(1) == True else print("Failed")
print("Success") if is_perfect_square(2) == False else print("Failed")
print("Success") if is_perfect_square(99) == False else print("Failed")
print("Success") if is_perfect_square(-9) == False else print("Failed")
print("Success") if is_perfect_square(0) == True else print("Failed")
print("Success") if is_perfect_square(25281) == True else print("Failed")