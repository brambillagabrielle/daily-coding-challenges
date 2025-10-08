'''
In day four of Space Week, you are given a matrix of numbers (an array of arrays), representing potential landing spots for your rover. Find the safest landing spot based on the following rules:
 - Each spot in the matrix will contain a number from 0-9, inclusive.
 - Any 0 represents a potential landing spot.
 - Any number other than 0 is too dangerous to land. The higher the number, the more dangerous.
 - The safest spot is defined as the 0 cell whose surrounding cells (up to 4 neighbors, ignore diagonals) have the lowest total danger.
 - Ignore out-of-bounds neighbors (corners and edges just have fewer neighbors).
 - Return the indices of the safest landing spot. There will always only be one safest spot.
 For instance, given:
    [
    [1, 0],
    [2, 0]
    ]
Return [0, 1], the indices for the 0 in the first array.
'''

def find_landing_spot(matrix):
    best_landing_spot = [0,0]
    least_danger = len(matrix) * 9

    ind_x = 0
    for i in matrix:
        ind_y = 0
        for j in i:
            if j == 0:
                total_danger = 0

                if ind_x - 1 > -1:
                    total_danger += matrix[ind_x - 1][ind_y]
                
                if ind_x + 1 < len(i):
                    total_danger += matrix[ind_x + 1][ind_y]

                if ind_y - 1 > -1:
                    total_danger += matrix[ind_x][ind_y - 1]
                
                if ind_y + 1 < len(i):
                    total_danger += matrix[ind_x][ind_y + 1]
                
                if total_danger < least_danger:
                    least_danger = total_danger
                    best_landing_spot = [ind_x, ind_y]
                
            ind_y += 1
        ind_x += 1

    return best_landing_spot

print("Success") if find_landing_spot([[1, 0], [2, 0]]) == [0, 1] else print("Failed")
print("Success") if find_landing_spot([[9, 0, 3], [7, 0, 4], [8, 0, 5]]) == [1, 1] else print("Failed")
print("Success") if find_landing_spot([[1, 2, 1], [0, 0, 2], [3, 0, 0]]) == [2, 2] else print("Failed")
print("Success") if find_landing_spot([[9, 6, 0, 8], [7, 1, 1, 0], [3, 0, 3, 9], [8, 6, 0, 9]]) == [2, 1] else print("Failed")