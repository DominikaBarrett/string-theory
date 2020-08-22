
import string

def text_process(text):
    letters = []
    for sign in text:
        if sign.isalpha() == True: #Jezeli prawda jest, ze 
            letters.append(sign.lower())
    text_processed = "".join(letters)
    return text_processed



def is_palindrome(text):

    """
    >>> is_palindrome('Mr. Owl ate my metal worm')
    True
    >>> is_palindrome('Eva, can I see bees in a cave?')
    True
    """

    text_processed = text_process(text)
    text_revers = text_processed[::-1]
    # print(text_original)
    # print(text_revers)
    return text_processed == text_revers

print(is_palindrome('Mr. Owl ate my metal worm'))
print(is_palindrome('Eva, can I see bees in a cave?'))



def is_isogram(text):
    """
    >>> is_isogram('uncopyrightables')
    True
    """
    unique_letters = set()
    letters = []
    for sign in text:
        if sign.isalpha() == True:
            unique_letters.add(sign.lower)
            letters.append(sign.lower())

    return len(letters) == len(unique_letters)

print(is_isogram('uncopyrightables'))

    

def is_pangram(text):
    """
    >>> is_pangram('The quick brown fox jumps over the lazy dog')
    True
    """
    alphabet = string.ascii_lowercase
    text_processed = text_process(text)
    text_processed_set = set(text_processed)
    # print(alphabet)
    # print(text_processed_set)
    if len(text_processed) != len(text_processed_set):
        return False
    text_processed = "".join(sorted(list(text_processed_set)))

    print(text_processed)

    

    return alphabet == text_processed

print(is_pangram('The quick brown fox jumps over the lazy dog'))


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
