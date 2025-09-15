'''
Given an input array of seven integers, representing a week's time, where each integer is the amount of hours spent on your phone that day, determine if it is too much screen time based on these constraints:

If any single day has 10 hours or more, it's too much.
If the average of any three days in a row is greater than or equal to 8 hours, it's too much.
If the average of the seven days is greater than or equal to 6 hours, it's too much.

'''

def too_much_screen_time(hours):
    is_too_much_screen_time = False

    ind = 0
    sum_hours = 0
    for h in hours:
        if h >= 10:
            is_too_much_screen_time = True

        try:
            average_3_days = (hours[ind - 2] + hours[ind - 1] + hours[ind]) / 3
            if average_3_days >= 8:
                is_too_much_screen_time = True
        except e:
            pass

        sum_hours += h
        ind += 1

    average_7_days = sum_hours / 7
    if average_7_days >= 6:
        is_too_much_screen_time = True

    return is_too_much_screen_time

print("Success") if too_much_screen_time([1, 2, 3, 4, 5, 6, 7]) == False else print("Failed")
print("Success") if too_much_screen_time([7, 8, 8, 4, 2, 2, 3]) == False else print("Failed")
print("Success") if too_much_screen_time([5, 6, 6, 6, 6, 6, 6]) == False else print("Failed")
print("Success") if too_much_screen_time([1, 2, 3, 11, 1, 3, 4]) == True else print("Failed")
print("Success") if too_much_screen_time([1, 2, 3, 10, 2, 1, 0]) == True else print("Failed")
print("Success") if too_much_screen_time([3, 3, 5, 8, 8, 9, 4]) == True else print("Failed")
print("Success") if too_much_screen_time([3, 9, 4, 8, 5, 7, 6]) == True else print("Failed")
