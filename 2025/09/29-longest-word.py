'''
Given a sentence, return the longest word in the sentence.
 - Ignore periods (.) when determining word length.
 - If multiple words are ties for the longest, return the first one that occurs.
'''

def get_longest_word(paragraph):
    word = ""
    longest_word = ""

    for p in paragraph:
        if p.isalpha():
            word += p
        else:
            if len(word) > len(longest_word):
                longest_word = word
            
            word = ""

    return longest_word

print("Success") if get_longest_word("coding is fun") == "coding" else print("Failed")
print("Success") if get_longest_word("Coding challenges are fun and educational.") == "educational" else print("Failed")
print("Success") if get_longest_word("This sentence has multiple long words.") == "sentence" else print("Failed")