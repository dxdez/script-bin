"""

    This is script is based off an example found online. The idea is to build an encoded string based on the number of unique characters within a given string. 

    For example if 'e' only occurs once in a string, then it is converted to '(' but if it occurs more than once then it is converted to ')'. This is only a just-for-fun example for playing around with the idea of manipulating string values. 

"""

# Duplicate Encode
# Constructs an encoded string based on the number of unique characters
#-----------------------
def duplicate_encode(word):
    word = word.lower()
    new_word = ""
    
    for character in word:
        if word.count(character) > 1:
            new_word += ")"
        else:
            new_word += "("
            
    return new_word


# Run user input
#-----------------------
print("------------------------------------------")
print("This program is used for testing duplicate encoding.")
print("Single occurences of a character will appear as '(' but more than one will appear as ')'.")
print("------------------------------------------")
current_input = input("Enter a phrase: ")

print("\nThe encoded phrase is: ")
print(duplicate_encode(current_input))
