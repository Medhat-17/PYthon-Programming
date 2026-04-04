 Advanced String Toolkit with ASCII Art
import pyfiglet  # pip install pyfiglet if needed
from collections import Counter

print(pyfiglet.figlet_format("Medhat's String Toolkit"))

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

def ascii_art(text):
    return pyfiglet.figlet_format(text)

def most_frequent_word(text):
    words = text.lower().split()
    if not words:
        return None
    counter = Counter(words)
    return counter.most_common(1)[0]

while True:
    print("\nChoose an option:")
    print("1. Reverse a string")
    print("2. Check if palindrome")
    print("3. Count characters")
    print("4. Count words")
    print("5. Uppercase")
    print("6. Lowercase")
    print("7. ASCII Art")
    print("8. Most Frequent Word")
    print("9. Exit")

    choice = input("Enter 1-9: ")

    if choice == "1":
        text = input("Enter string to reverse: ")
        print("Reversed string:", text[::-1])

    elif choice == "2":
        text = input("Enter string to check palindrome: ")
        print(f"'{text}' is a palindrome!" if is_palindrome(text) else f"'{text}' is NOT a palindrome.")

    elif choice == "3":
        text = input("Enter string to count characters: ")
        print("Number of characters:", len(text))

    elif choice == "4":
        text = input("Enter string to count words: ")
        print("Number of words:", len(text.split()))

    elif choice == "5":
        text = input("Enter string to convert to uppercase: ")
        print("Uppercase:", text.upper())

    elif choice == "6":
        text = input("Enter string to convert to lowercase: ")
        print("Lowercase:", text.lower())

    elif choice == "7":
        text = input("Enter string for ASCII art: ")
        print(ascii_art(text))

    elif choice == "8":
        text = input("Enter string to find most frequent word: ")
        result = most_frequent_word(text)
        if result:
            print(f"Most frequent word: '{result[0]}' occurred {result[1]} times")
        else:
            print("No words found!")

    elif choice == "9":
        print("Exiting String Toolkit. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter 1-9.")
