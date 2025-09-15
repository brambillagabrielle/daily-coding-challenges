'''
Given the current temperature of a room and a target temperature, return a string indicating how to adjust the room temperature based on these constraints:
 - Return "heat" if the current temperature is below the target.
 - Return "cool" if the current temperature is above the target.
 - Return "hold" if the current temperature is equal to the target.
'''

def adjust_thermostat(temp, target):
    indication = ""

    if temp < target:
        indication = "heat"
    elif temp > target:
        indication = "cool"
    else:
        indication = "hold"

    return indication

print("Success") if adjust_thermostat(68, 72) == "heat" else print("Failed")
print("Success") if adjust_thermostat(75, 72) == "cool" else print("Failed")
print("Success") if adjust_thermostat(72, 72) == "hold" else print("Failed")
print("Success") if adjust_thermostat(-20.5, -10.1) == "heat" else print("Failed")
print("Success") if adjust_thermostat(100, 99.9) == "cool" else print("Failed")
print("Success") if adjust_thermostat(0.0, 0.0) == "hold" else print("Failed")