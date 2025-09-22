'''
Given a string, return "digits" if the string has more digits than letters, "letters" if it has more letters than digits, and "tie" if it has the same amount of digits and letters.
 - Digits consist of 0-9.
 - Letters consist of a-z in upper or lower case.
 - Ignore any other characters.
'''

def digits_or_letters(str):
    cont_digits = 0
    cont_letters = 0

    for s in str:
        if s.isnumeric():
            cont_digits += 1
        elif s.isalpha():
            cont_letters += 1

    if cont_digits > cont_letters:
        return "digits"
    elif cont_digits < cont_letters:
        return "letters"
    else:
        return "tie"

print("Success") if digits_or_letters("abc123") == "tie" else print("Failed")
print("Success") if digits_or_letters("a1b2c3d") == "letters" else print("Failed")
print("Success") if digits_or_letters("1a2b3c4") == "digits" else print("Failed")
print("Success") if digits_or_letters("abc123!@#DEF") == "letters" else print("Failed")
print("Success") if digits_or_letters("H3110 W0R1D") == "digits" else print("Failed")
print("Success") if digits_or_letters("P455W0RD") == "tie" else print("Failed")