# A simple function for generating hashtags

def generate_hashtag(s):
    # Check if the input string is empty or None
    if not s:
        return False

    # Capitalize the first letter of each word, join them, and add a hashtag
    hashtag = '#' + ''.join(word.capitalize() for word in s.split())

    # Check if the resulting hashtag is longer than 140 characters
    if len(hashtag) > 140:
        return False

    return hashtag
