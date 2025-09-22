'''
Given a video size, a unit for the video size, a hard drive capacity, and a unit for the hard drive, return the number of videos the hard drive can store using the following constraints:
 - The unit for the video size can be bytes ("B"), kilobytes ("KB"), megabytes ("MB"), or gigabytes ("GB").
 - If not given one of the video units above, return "Invalid video unit".
 - The unit of the hard drive capacity can be gigabytes ("GB") or terabytes ("TB").
 - If not given one of the hard drive units above, return "Invalid drive unit".
 - Return the number of whole videos the drive can fit.
 - Use the following conversions:
     ___________________________
    |   Unit    |   Equivalent  |
    |   1B      |   1B          |
    |   1KB     |   1000B       |
    |   1MB     |   1000KB      |
    |   1GB     |   1000MB      |
    |   1TB     |   1000GB      |
     ---------------------------
 - For example, given 500, "MB", 100, and "GB as arguments, determine how many 500 MB videos can fit on a 100 GB hard drive.
'''

def number_of_videos(video_size, video_unit, drive_size, drive_unit):
    unit_dict_gb = {
        "B": 1000000000,
        "KB": 1000000,
        "MB": 1000,
        "GB": 1
    }
    video_size_conversion = 0

    if video_unit != "KB" and video_unit != "MB" and video_unit != "GB":
        return "Invalid video unit"
    
    if drive_unit == "GB":
        video_size_conversion = video_size / unit_dict_gb[video_unit]
    elif drive_unit == "TB":
        video_size_conversion = video_size / (unit_dict_gb[video_unit] * 1000)
    else:
        return "Invalid drive unit"

    return int(drive_size / video_size_conversion)

print("Success") if number_of_videos(500, "MB", 100, "GB") == 200 else print("Failed")
print("Success") if number_of_videos(2000, "B", 1, "TB") == "Invalid video unit" else print("Failed")
print("Success") if number_of_videos(2000, "MB", 100000, "MB") == "Invalid drive unit" else print("Failed")
print("Success") if number_of_videos(500000, "KB", 2, "TB") == 4000 else print("Failed")
print("Success") if number_of_videos(1.5, "GB", 2.2, "TB") == 1466 else print("Failed")