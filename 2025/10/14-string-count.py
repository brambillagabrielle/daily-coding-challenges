'''
Given two strings, determine how many times the second string appears in the first.
 - The pattern string can overlap in the first string. For example, "aaa" contains "aa" twice. The first two a's and the second two.
'''

def count(text, parameter):
    pattern_count = 0
    
    ind = 0
    for t in text:
        if t == parameter[0] and ind <= len(text) - len(parameter):
            same_pattern = True

            ind_aux = ind
            for p in parameter:
                if p != text[ind_aux]:
                    same_pattern = False
                
                ind_aux += 1

            if same_pattern:
                pattern_count += 1

        ind += 1

    return pattern_count

print("Success") if count('abcdefg', 'def') == 1 else print("Failed")
print("Success") if count('hello', 'world') == 0 else print("Failed")
print("Success") if count('mississippi', 'iss') == 2 else print("Failed")
print("Success") if count('she sells seashells by the seashore', 'sh') == 3 else print("Failed")
print("Success") if count('101010101010101010101', '101') == 10 else print("Failed")