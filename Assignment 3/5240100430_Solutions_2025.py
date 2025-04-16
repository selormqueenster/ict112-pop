"""
Solutions to assignment 3
"""

"""
1.Write a Python program to reverse the string "Programming". Print the reversed string.
Hint: Use string slicing or a loop.
"""
# Original string
original_string = "Programming"

# Reversing the string using slicing
reversed_string = original_string[::-1]

# Printing the reversed string
print(reversed_string)


"""
2.Create a Python program that takes a user’s full name as input and prints the initials in uppercase.
Example: Input: "john doe", Output: "J.D."
"""
def get_initials(full_name):
    # Split the full name into parts
    name_parts = full_name.split()
    # Extract the initials and convert to uppercase
    initials = [part[0].upper() for part in name_parts]
    # Join the initials with dots
    return '.'.join(initials) + '.'

# Get user input
user_input = input("Enter your full name: ")
# Print the initials
print(get_initials(user_input))


"""
3.Write a Python program to check if a given string is a palindrome. A palindrome reads the same forwards
and backward (e.g., "radar", "level"). Hint: Compare the string with its reverse.
"""

def is_palindrome(s):
    # Remove spaces and convert to lowercase for uniformity
    cleaned_string = ''.join(s.split()).lower()
    # Compare the string with its reverse
    return cleaned_string == cleaned_string[::-1]

# Example usage
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print(f'"{input_string}" is a palindrome.')
else:
    print(f'"{input_string}" is not a palindrome.')

"""
4.Create a Python program that asks the user to enter a sentence and counts the number of words in the sentence.
Hint: Use the split() method to break the string into words.
"""
# Program to count the number of words in a sentence

# Ask the user to enter a sentence
sentence = input("Please enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Count the number of words
word_count = len(words)

# Display the result
print(f"The number of words in the sentence is: {word_count}")


"""
5.Write a Python program to replace all occurrences of "is" with "was" in the string "This is a string and it
is an example." Print the modified string.
# Original string
original_string = "This is a string and it is an example."

# Replace occurrences of 'is' with 'was'
modified_string = original_string.replace("is", "was")

# Print the modified string
print(modified_string)
"""
