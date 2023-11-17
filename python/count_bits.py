# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number. You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case

def count_bits(n):
    # Convert the integer to binary and count the '1' bits
    return bin(n).count('1')

# Example usage:
# result = count_bits(1234)
# print(result)  # Output: 5

