'''
Given two strings, determine if the second string is a mirror of the first.
 - A string is considered a mirror if it contains the same letters in reverse order.
 - Treat uppercase and lowercase letters as distinct.
 - Ignore all non-alphabetical characters.
'''

def is_mirror(str1, str2):
    cleaned_str1 = ""    
    for s in str1:
        if s.isalpha():
            cleaned_str1 += s

    cleaned_str2 = ""
    for s in str2:
        if s.isalpha():
            cleaned_str2 += s

    if len(cleaned_str1) != len(cleaned_str2):
        return False
    else:
        ind = 0
        for s in cleaned_str1:
            if s != cleaned_str2[len(cleaned_str2) - ind - 1]:
                return False
            ind += 1

    return True

print("Success") if is_mirror("helloworld", "helloworld") == False else print("Failed")
print("Success") if is_mirror("Hello World", "dlroW olleH") == True else print("Failed")
print("Success") if is_mirror("RaceCar", "raCecaR") == True else print("Failed")
print("Success") if is_mirror("RaceCar", "RaceCar") == False else print("Failed")
print("Success") if is_mirror("Mirror", "rorrim") == False else print("Failed")
print("Success") if is_mirror("Hello World", "dlroW-olleH") == True else print("Failed")
print("Success") if is_mirror("Hello World", "!dlroW !olleH") == True else print("Failed")