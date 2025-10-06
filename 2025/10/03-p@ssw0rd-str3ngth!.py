'''
Given a password string, return "weak", "medium", or "strong" based on the strength of the password.
A password is evaluated according to the following rules:
 - It is at least 8 characters long.
 - It contains both uppercase and lowercase letters.
 - It contains at least one number.
 - It contains at least one special character from this set: !, @, #, $, %, ^, &, or *.
Return "weak" if the password meets fewer than two of the rules. Return "medium" if the password meets 2 or 3 of the rules. Return "strong" if the password meets all 4 rules.
'''

def check_strength(password):
    contain_upper = False
    contain_lower = False
    contain_number = False
    contain_special_char = False
    special_char = ["!","@","#","$","%","^","&","*"]

    for p in password:
        if p.isupper():
            contain_upper = True
        elif p.islower():
            contain_lower = True
        elif p.isnumeric():
            contain_number = True
        elif p in special_char:
            contain_special_char = True
    
    count_rules_met = 0
    if len(password) > 8:
        count_rules_met += 1

    if contain_upper and contain_lower:
        count_rules_met += 1

    if contain_number:
        count_rules_met += 1

    if contain_special_char:
        count_rules_met += 1
    
    strength_level = ""
    if count_rules_met < 2:
        strength_level = "weak"
    elif count_rules_met == 2 or count_rules_met == 3:
        strength_level = "medium"
    else:
        strength_level = "strong"

    return strength_level

print("Success") if check_strength("123456") == "weak" else print("Failed")
print("Success") if check_strength("pass!!!") == "weak" else print("Failed")
print("Success") if check_strength("Qwerty") == "weak" else print("Failed")
print("Success") if check_strength("PASSWORD") == "weak" else print("Failed")
print("Success") if check_strength("PASSWORD!") == "medium" else print("Failed")
print("Success") if check_strength("PassWord%^!") == "medium" else print("Failed")
print("Success") if check_strength("qwerty12345") == "medium" else print("Failed")
print("Success") if check_strength("PASSWORD!") == "medium" else print("Failed")
print("Success") if check_strength("PASSWORD!") == "medium" else print("Failed")
print("Success") if check_strength("S3cur3P@ssw0rd") == "strong" else print("Failed")
print("Success") if check_strength("C0d3&Fun!") == "strong" else print("Failed")