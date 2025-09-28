'''
Given a phone number in the format "+A (BBB) CCC-DDDD", where each letter represents a digit as follows:
 - A represents the country code and can be any number of digits.
 - BBB represents the area code and will always be three digits.
 - CCC and DDDD represent the local number and will always be three and four digits long, respectively.
Determine if it's a spam number based on the following criteria:
 - The country code is greater than 2 digits long or doesn't begin with a zero (0).
 - The area code is greater than 900 or less than 200.
 - The sum of first three digits of the local number appears within last four digits of the local number.
 - The number has the same digit four or more times in a row (ignoring the formatting characters).
'''

def is_spam(number):
    is_country_code = True
    count_country_code = 0

    is_area_code = False
    area_code_digits = ""

    is_local_number = False
    sum_local_digits = 0
    is_last_local_digits = False

    previous_digit = 0
    count_same_digit = 1

    for n in number:
        if is_country_code:
            if count_country_code == 1 and n != "0":
                return True
            
            if n == " ":
                is_country_code = False
                is_area_code = True
            elif count_country_code > 2:
                return True

            count_country_code += 1

        elif is_area_code:
            if n == "(" or n == ")":
                continue
            elif n == " ":
                if int(area_code_digits) < 200 or int(area_code_digits) > 900:
                    return True

                is_area_code = False
                is_local_number = True
            else:
                area_code_digits += n

        elif is_local_number:
            if n == "-":
                is_last_local_digits = True
            elif is_last_local_digits:
                if n == str(sum_local_digits):
                    return True
            else:
                sum_local_digits += int(n)

        if n.isnumeric():
            if n == previous_digit:
                count_same_digit += 1
            else:
                count_same_digit = 1

            if count_same_digit >= 4:
                return True
            
            previous_digit = n

    return False

print("Success") if is_spam("+0 (200) 234-0182") == False else print("Failed")
print("Success") if is_spam("+091 (555) 309-1922") == True else print("Failed")
print("Success") if is_spam("+1 (555) 435-4792") == True else print("Failed")
print("Success") if is_spam("+0 (955) 234-4364") == True else print("Failed")
print("Success") if is_spam("+0 (155) 131-6943") == True else print("Failed")
print("Success") if is_spam("+0 (155) 131-6943") == True else print("Failed")
print("Success") if is_spam("+0 (555) 135-0192") == True else print("Failed")
print("Success") if is_spam("+0 (555) 564-1987") == True else print("Failed")
print("Success") if is_spam("+00 (555) 234-0182") == False else print("Failed")