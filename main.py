def odds_sum(L):
    """Return the sum of the odd elements of L."""
    return sum([i for i in L if i % 2 != 0])

def has_letter_cases(s: str):
    """
    Return True if and only if s contains at least one lowercase letter and at 
    least one uppercase letter.
    """
    return not s.isupper() and not s.islower()

def find_lowercase_vowel(msg: str):
    """
    Return the index of the first lowercase vowel (a, e, i, o, u) in msg, 
    or the length of msg if it does not contain any lowercase vowels.
    """
    for index, char in enumerate(msg):
        if char in 'aeiou':
            return index
    return len(msg)
def print_name(name):
    
    return "hi name"
