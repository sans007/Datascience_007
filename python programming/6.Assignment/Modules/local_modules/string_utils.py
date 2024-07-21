# string_utils.py

def reverse_string(s):
    return s[::-1]

def capitalize_string(s):
    
    return s.capitalize()

def to_uppercase(s):
    
    return s.upper()

def to_lowercase(s):
    
    return s.lower()

def count_vowels(s):
    
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)
