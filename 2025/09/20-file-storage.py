'''
Given a file size, a unit for the file size, and hard drive capacity in gigabytes (GB), return the number of files the hard drive can store using the following constraints:
 - The unit for the file size can be bytes ("B"), kilobytes ("KB"), or megabytes ("MB").
 - Return the number of whole files the drive can fit.
 - Use the following conversions:
     ___________________________
    |   Unit    |   Equivalent  |
    |   1B      |   1B          |
    |   1KB     |   1000B       |
    |   1MB     |   1000KB      |
    |   1GB     |   1000MB      |
     ---------------------------
 - For example, given 500, "KB", and 1 as arguments, determine how many 500 KB files can fit on a 1 GB hard drive.
'''

def number_of_files(file_size, file_unit, drive_size_gb):
    file_size_conversion = 0

    if file_unit == "B":
        file_size_conversion = file_size / 1000000000
    elif file_unit == "KB":
        file_size_conversion = file_size / 1000000
    elif file_unit == "MB":
        file_size_conversion = file_size / 1000

    return int(drive_size_gb / file_size_conversion)

print("Success") if number_of_files(500, "KB", 1) == 2000 else print("Failed")
print("Success") if number_of_files(50000, "B", 1) == 20000 else print("Failed")
print("Success") if number_of_files(5, "MB", 1) == 200 else print("Failed")
print("Success") if number_of_files(4096, "B", 1.5) == 366210 else print("Failed")
print("Success") if number_of_files(220.5, "KB", 100) == 453514 else print("Failed")
print("Success") if number_of_files(4.5, "MB", 750) == 166666 else print("Failed")