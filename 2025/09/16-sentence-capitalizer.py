'''
Given a paragraph, return a new paragraph where the first letter of each sentence is capitalized.
 - All other characters should be preserved.
 - Sentences can end with a period (.), one or more question marks (?), or one or more exclamation points (!).
'''

def capitalize(paragraph):
    capitalized_paragraph = ""

    ind = 0
    sentence_ind = 0
    for p in paragraph:
        if (ind == 0 or sentence_ind == 0) and p.isalpha():
            capitalized_paragraph += p.upper()
            sentence_ind += 1
        elif ind == len(paragraph) - 1:
            capitalized_paragraph += p
        else:
            if p == "." or p == "?" or p == "!":
                if paragraph[ind + 1] == " ":
                    sentence_ind = -1
                else:
                    sentence_ind = 0
            else:
                sentence_ind += 1
            
            capitalized_paragraph += p
            
        ind += 1
    
    return capitalized_paragraph

print("Success") if capitalize("this is a simple sentence.") == "This is a simple sentence." else print("Failed")
print("Success") if capitalize("hello world. how are you?") == "Hello world. How are you?" else print("Failed")
print("Success") if capitalize("i did today's coding challenge... it was fun!!") == "I did today's coding challenge... It was fun!!" else print("Failed")
print("Success") if capitalize("crazy!!!strange???unconventional...sentences.") == "Crazy!!!Strange???Unconventional...Sentences." else print("Failed")
print("Success") if capitalize("there's a space before this period . why is there a space before that period ?")== "There's a space before this period . Why is there a space before that period ?" else print("Failed")