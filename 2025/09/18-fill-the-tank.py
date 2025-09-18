'''
Given the size of a fuel tank, the current fuel level, and the price per gallon, return the cost to fill the tank all the way.
 - tankSize is the total capacity of the tank in gallons.
 - fuelLevel is the current amount of fuel in the tank in gallons.
 - pricePerGallon is the cost of one gallon of fuel.
 - The returned value should be rounded to two decimal places in the format: "$d.dd".
'''

def cost_to_fill(tank_size, fuel_level, price_per_gallon):
    cost_to_fill = 0
    dif_tank = tank_size - fuel_level

    if dif_tank > 0:
        cost_to_fill = dif_tank * price_per_gallon

    return "${:.2f}".format(cost_to_fill)

print("Success") if cost_to_fill(20, 0, 4.00) == "$80.00" else print("Failed")
print("Success") if cost_to_fill(15, 10, 3.50) == "$17.50" else print("Failed")
print("Success") if cost_to_fill(18, 9, 3.25) == "$29.25" else print("Failed")
print("Success") if cost_to_fill(12, 12, 4.99) == "$0.00" else print("Failed")
print("Success") if cost_to_fill(15, 9.5, 3.98) == "$21.89" else print("Failed")