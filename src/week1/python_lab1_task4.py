"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

def count_characters(text):
    """Count non-space characters in a string."""
    count = 0
    for ch in text:
        if ch != " ":
            count += 1
    return count

def count_words(text):
    """Count the number of words in a string."""
    return len(text.split())

def extract_numbers(text):
    """Return a list of integers found in the text."""
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers

def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    chars = count_characters(text)
    words = count_words(text)
    numbers = extract_numbers(text)

    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else 0

    return chars, words, numbers, total, average


# Main program
sentence = input("Enter a sentence with numbers: ")

chars, words, numbers, total, avg = analyze_text(sentence)

print("\n--- Text Analysis ---")
print("Non-space characters:", chars)
print("Word count:", words)
print("Numbers found:", numbers if numbers else "None")
print("Sum of numbers:", total)
print("Average of numbers:", f"{avg:.2f}" if numbers else "N/A")