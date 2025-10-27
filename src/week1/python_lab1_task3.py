"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""

def analyze_sentence(text):
    # Count total characters
    char_count = len(text)

    # Count total words
    words = text.split()
    word_count = len(words)

    # Check if the sentence contains "Python" (not case-sensitive)
    contains_python = "python" in text.lower()

    return char_count, word_count, contains_python


# Main program
sentence = input("Enter a sentence: ")

length, count, has_python = analyze_sentence(sentence)

print("Total characters:", length)
print("Total words:", count)
print("Contains 'Python':", has_python)