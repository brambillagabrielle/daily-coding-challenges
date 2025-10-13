'''
For day six of Space Week, you will be given a date in the format "YYYY-MM-DD" and need to determine the phase of the moon for that day using the following rules:
Use a simplified lunar cycle of 28 days, divided into four equal phases:
 - "New": days 1 - 7
 - "Waxing": days 8 - 14
 - "Full": days 15 - 21
 - "Waning": days 22 - 28
After day 28, the cycle repeats with day 1, a new moon.
 - Use "2000-01-06" as a reference new moon (day 1 of the cycle) to determine the phase of the given day.
 - You will not be given any dates before the reference date.
 - Return the correct phase as a string.
'''

from datetime import timedelta, datetime

def moon_phase(date_string):
    sepatered_string = date_string.split("-")
    date = datetime(int(sepatered_string[0]), int(sepatered_string[1]), int(sepatered_string[2]))
    ref_date = datetime(2000, 1, 6)

    phase = 1
    while True:
        ref_date = ref_date + timedelta(days = 7)
        if date < ref_date:
            break

        if phase < 4:
            phase += 1
        else:
            phase = 1

    if phase == 1:
        return "New"
    elif phase == 2:
        return "Waxing"
    elif phase == 3:
        return "Full"
    else:
        return "Waning"

print("Success") if moon_phase("2000-01-12") == "New" else print("Failed")
print("Success") if moon_phase("2000-01-13") == "Waxing" else print("Failed")
print("Success") if moon_phase("2014-10-15") == "Full" else print("Failed")
print("Success") if moon_phase("2012-10-21") == "Waning" else print("Failed")
print("Success") if moon_phase("2022-12-14") == "New" else print("Failed")