'''
Given a string representing a time of the day in the 24-hour format of "HHMM", return the time in its equivalent 12-hour format of "H:MM AM" or "H:MM PM".
 - The given input will always be a four-digit string in 24-hour time format, from "0000" to "2359".
'''

def to_12(time):
    hour = time[0] + time[1]
    minute = time[2] + time[3]

    converted_hour = ""
    am_or_pm = "AM"

    if int(hour) == 0:
        converted_hour += "12"
    elif int(hour) < 12:
        converted_hour += str(int(hour))
    else:
        converted_hour += str(int(hour) - 12)
        am_or_pm = "PM"

    return converted_hour + ":" + minute + " " + am_or_pm

print("Success") if to_12("1124") == "11:24 AM" else print("Failed")
print("Success") if to_12("0900") == "9:00 AM" else print("Failed")
print("Success") if to_12("1455") == "2:55 PM" else print("Failed")
print("Success") if to_12("2346") == "11:46 PM" else print("Failed")
print("Success") if to_12("0030") == "12:30 AM" else print("Failed")