
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def reverse_string(s):
    return s[::-1]    


def is_palindrome(s):
    cleaned_string = ''.join(s.split()).lower()
    return cleaned_string == cleaned_string[::-1]

def capitalize_words(s):
    return ' '.join(word.capitalize() for word in s.split())

def count_words(s):
    return len(s.split())

def remove_whitespace(s):
    return ''.join(s.split())

def replace_substring(s, old, new):
    return s.replace(old, new)

def find_substring(s, substring):
    return s.find(substring)

def count_occurrences(s, substring):
    return s.count(substring)

def to_uppercase(s):
    return s.upper()
