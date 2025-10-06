'''
For the second day of Space Week, you are given a string where each character represents the luminosity reading of a star. Determine if the readings have detected an exoplanet using the transit method. The transit method is when a planet passes in front of a star, reducing its observed luminosity.
 - Luminosity readings only comprise of characters 0-9 and A-Z where each reading corresponds to the following numerical values:
 - Characters 0-9 correspond to luminosity levels 0-9.
 - Characters A-Z correspond to luminosity levels 10-35.
A star is considered to have an exoplanet if any single reading is less than or equal to 80% of the average of all readings. For example, if the average luminosity of a star is 10, it would be considered to have a exoplanet if any single reading is 8 or less.
'''

def has_exoplanet(readings):
    sum = 0
    for r in readings:
        try:
            sum += int(r)
        except:
            sum += ord(r)%32 + 9

    average = sum / len(readings)
    average_80_perc = average * 0.8

    for r in readings:
        try:
            if int(r) <= average_80_perc:
                return True
        except:
            if ord(r)%32 + 9 <= average_80_perc:
                return True
    
    return False

print("Success") if has_exoplanet("665544554") == False else print("Failed")
print("Success") if has_exoplanet("FGFFCFFGG") == True else print("Failed")
print("Success") if has_exoplanet("MONOPLONOMONPLNOMPNOMP") == False else print("Failed")
print("Success") if has_exoplanet("FREECODECAMP") == True else print("Failed")
print("Success") if has_exoplanet("9AB98AB9BC98A") == False else print("Failed")
print("Success") if has_exoplanet("ZXXWYZXYWYXZEGZXWYZXYGEE") == True else print("Failed")