'''
Given a string of ten digits, return the string as a phone number in this format: "+D (DDD) DDD-DDDD".
'''

def format_number(number):
    formatted_number = ""

    cont = 0
    for n in number:
        if cont == 0:
            formatted_number = "+" + n
        elif cont == 1:
            formatted_number += " (" + n
        elif cont == 3:
            formatted_number += n + ") "
        elif cont == 7:
            formatted_number += "-" + n
        else:
            formatted_number += n

        cont += 1

    return formatted_number

print("Success") if format_number("05552340182") == "+0 (555) 234-0182" else print("Failed")
print("Success") if format_number("15554354792") == "+1 (555) 435-4792" else print("Failed")