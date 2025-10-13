'''
Given a string representing a hexadecimal number (base 16), return its decimal (base 10) value as an integer.
Hexadecimal is a number system that uses 16 digits:
 - 0-9 represent values 0 through 9.
 - A-F represent values 10 through 15.
Here's a partial conversion table:

    Hexadecimal	Decimal
    0	0
    1	1
    ...	...
    9	9
    A	10
    ...	...
    F	15
    10	16
    ...	...
    9F	159
    A0	160
    ...	...
    FF	255
    100	256

 - The string will only contain characters 0-9 and A-F.
'''

def hex_to_decimal(hex):
    hex_letters = {
        "A": 10,
        "B": 11,
        "C": 12,
        "D": 13,
        "E": 14,
        "F": 15
    }

    decimal = 0
    base_16 = 1
    for i in range(len(hex) - 1, -1, -1):
        if int(hex[i].isnumeric()):
            decimal += int(hex[i]) * base_16
        else:
            decimal += int(hex_letters[hex[i]]) * base_16

        base_16 *= 16

    return decimal

print("Success") if hex_to_decimal("A") == 10 else print("Failed")
print("Success") if hex_to_decimal("15") == 21 else print("Failed")
print("Success") if hex_to_decimal("2E") == 46 else print("Failed")
print("Success") if hex_to_decimal("FF") == 255 else print("Failed")
print("Success") if hex_to_decimal("A3F") == 2623 else print("Failed")