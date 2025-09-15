'''
Given a paragraph, return an array of the three most frequently occurring words.
 - Words in the paragraph will be separated by spaces.
 - Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
 - Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
 - The returned array should have all lowercase words.
 - The returned array should be in descending order with the most frequently occurring word first.
'''

def get_words(paragraph):
    separated_words = []
    word_count = {}
    word = ""
    most_frequent_words = []

    for p in paragraph:
        if p.isalpha():
            word += p.lower()
        else:
            if word != "":
                separated_words.append(word)
                word = ""

    for w in separated_words:
        count = 0

        for c in separated_words:
            if c == w:
                count += 1

        word_count[w] = count

    word_count_sorted = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    for key, value in word_count_sorted:
        most_frequent_words.append(key)

    return most_frequent_words[:3]

print("Success") if get_words("Coding in Python is fun because coding Python allows for coding in Python easily while coding") == ["coding", "python", "in"] else print("Failed")
print("Success") if get_words("I like coding. I like testing. I love debugging!") == ["i", "like", "coding"] else print("Failed")
print("Success") if get_words("Debug, test, deploy. Debug, debug, test, deploy. Debug, test, test, deploy!") == ["debug", "test", "deploy"] else print("Failed")