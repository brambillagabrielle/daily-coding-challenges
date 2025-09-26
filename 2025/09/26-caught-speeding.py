'''
Given an array of numbers representing the speed at which vehicles were observed traveling, and a number representing the speed limit, return an array with two items, the number of vehicles that were speeding, followed by the average amount beyond the speed limit of those vehicles.
 - If there were no vehicles speeding, return [0, 0].
'''

def speeding(speeds, limit):
    cont_vehicles = 0
    beyond_speed_limit = 0

    for s in speeds:
        if s > limit:
            beyond_speed_limit += s - limit
            cont_vehicles += 1

    if cont_vehicles > 0:
        return [cont_vehicles, (beyond_speed_limit / cont_vehicles)]
    else:
        return [0,0]

print("Success") if speeding([50, 60, 55], 60) == [0, 0] else print("Failed")
print("Success") if speeding([58, 50, 60, 55], 55) == [2, 4] else print("Failed")
print("Success") if speeding([61, 81, 74, 88, 65, 71, 68], 70) == [4, 8.5] else print("Failed")
print("Success") if speeding([100, 105, 95, 102], 100) == [2, 3.5] else print("Failed")
print("Success") if speeding([40, 45, 44, 50, 112, 39], 55) == [1, 57] else print("Failed")