def is_palindrome(text):
    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """

    letters = []
    for sign in text:
        if sign.isalpha() == True: #Jezeli prawda jest, ze 
            letters.append(sign.lower())
    
    text_original = "".join(letters)
    text_revers = "".join(reversed(letters))
    # print(text_original)
    # print(text_revers)
    return text_original == text_revers

print(is_palindrome('Mr. Owl ate my metal worm'))
print(is_palindrome('Eva, can I see bees in a cave?'))



def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    pass


def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    pass


def is_anagram(text1, text2):
    """
    >>> is_anagram('Justin Timberlake', "I'm a jerk but listen")
    True
    """
    pass


def is_blanagram(text1, text2):
    """
    >>> is_blanagram('Justin Timberlake', "I'm a berk but listen")
    True
    """
    pass
