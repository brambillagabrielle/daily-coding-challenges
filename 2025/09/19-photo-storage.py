'''
Given a photo size in megabytes (MB), and hard drive capacity in gigabytes (GB), return the number of photos the hard drive can store using the following constraints:
 - 1 gigabyte equals 1000 megabytes.
 - Return the number of whole photos the drive can store.
'''

def number_of_photos(photo_size_mb, drive_size_gb):
    drive_size_mb = drive_size_gb * 1000
    return int(drive_size_mb / photo_size_mb)

print("Success") if number_of_photos(1, 1) == 1000 else print("Failed")
print("Success") if number_of_photos(2, 1) == 500 else print("Failed")
print("Success") if number_of_photos(4, 256) == 64000 else print("Failed")
print("Success") if number_of_photos(3.5, 750) == 214285 else print("Failed")
print("Success") if number_of_photos(3.5, 5.5) == 1571 else print("Failed")