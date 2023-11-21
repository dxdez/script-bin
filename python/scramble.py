# This function true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

def scramble(s1, s2):
    # Count the occurrences of each character in s1
    count_s1 = {}
    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1

    # Count the occurrences of each character in s2
    count_s2 = {}
    for char in s2:
        count_s2[char] = count_s2.get(char, 0) + 1

    # Check if there are enough characters in s1 to form s2
    for char, count in count_s2.items():
        if count_s1.get(char, 0) < count:
            return False

    return True

# Test cases
print(scramble('rkqodlw', 'world'))  # True
print(scramble('cedewaraaossoqqyt', 'codewars'))  # True
print(scramble('katas', 'steak'))  # False

