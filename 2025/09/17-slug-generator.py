'''
Given a string, return a URL-friendly version of the string using the following constraints:
 - All letters should be lowercase.
 - All characters that are not letters, numbers, or spaces should be removed.
 - All spaces should be replaced with the URL-encoded space code %20.
 - Consecutive spaces should be replaced with a single %20.
 - The returned string should not have leading or trailing %20.
'''

def generate_slug(str):
    cleaned_str = ""
    
    ind = 0
    is_leading_spaces = False
    consecutive_spaces = 0
    
    for s in str:
        if s == " ":
            if ind == 0:
                is_leading_spaces = True
            
            if ind == len(str) - 1:
                break
            
            if str[ind + 1].isalnum() and is_leading_spaces == 0:
                cleaned_str += "%20"

            consecutive_spaces += 1
        elif s.isalpha():
            is_leading_spaces = False
            consecutive_spaces = 0

            cleaned_str += s.lower()
        elif s.isnumeric():
            is_leading_spaces = False
            consecutive_spaces = 0

            cleaned_str += s

        ind += 1 

    return cleaned_str

print("Success") if generate_slug("helloWorld") == "helloworld" else print("Failed")
print("Success") if generate_slug("hello world!") == "hello%20world" else print("Failed")
print("Success") if generate_slug(" hello-world ") == "helloworld" else print("Failed")
print("Success") if generate_slug("hello  world") == "hello%20world" else print("Failed")
print("Success") if generate_slug("  ?H^3-1*1]0! W[0%R#1]D  ") == "h3110%20w0r1d" else print("Failed")