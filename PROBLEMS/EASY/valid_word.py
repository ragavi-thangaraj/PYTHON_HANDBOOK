
# LEETCODE QUESTION
# 3136. Valid Word

# A word is considered valid if:

# It contains a minimum of 3 characters.
# It contains only digits (0-9), and English letters (uppercase and lowercase).
# It includes at least one vowel.
# It includes at least one consonant.


def valid(word : str) -> bool:
    if len(word)<3:
        return False
    vowels= set('aeiouAEIOU')
    has_vowel = False
    has_consonant = False
    for ch in word:
        if not ch.isalnum():
            return False
        if ch.isalnum():
            if ch in vowels:
                has_vowel = True
            else:
                has_consonant = True
    return has_vowel and has_consonant


w = input("Enter Password : ")
print(valid(w))


# Sample Input Output :

# Enter Password : H2o
# True

# Enter Password : h8
# False
