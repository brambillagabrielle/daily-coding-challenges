'''
For the fifth day of Space Week, you will calculate the "Goldilocks zone" of a star - the region around a star where conditions are "just right" for liquid water to exist.
Given the mass of a star, return an array with the start and end distances of its Goldilocks Zone in Astronomical Units.
To calculate the Goldilocks Zone:
    1. Find the luminosity of the star by raising its mass to the power of 3.5.
    2. The start of the zone is 0.95 times the square root of its luminosity.
    3. The end of the zone is 1.37 times the square root of its luminosity.
 - Return the distances rounded to two decimal places.
For example, given 1 as a mass, return [0.95, 1.37].
'''

def goldilocks_zone(mass):
    luminosity = mass ** 3.5
    start_zone = 0.95 * (luminosity ** (1/2))
    end_zone = 1.37 * (luminosity ** (1/2))

    return [round(start_zone, 2), round(end_zone, 2)]

print("Success") if goldilocks_zone(1) == [0.95, 1.37] else print("Failed")
print("Success") if goldilocks_zone(0.5) == [0.28, 0.41] else print("Failed")
print("Success") if goldilocks_zone(6) == [21.85, 31.51] else print("Failed")
print("Success") if goldilocks_zone(3.7) == [9.38, 13.52] else print("Failed")
print("Success") if goldilocks_zone(20) == [179.69, 259.13] else print("Failed")