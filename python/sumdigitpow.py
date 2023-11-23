# We need a function to collect numbers, that may receive two integers a, b that defines the range [a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.
# Examples:
# -  1, 10  --> [1, 2, 3, 4, 5, 6, 7, 8, 9]
# -  1, 100 --> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

def sum_dig_pow(a, b):
    result = []

    for num in range(a, b + 1):
        num_str = str(num)
        if num == sum(int(digit) ** (index + 1) for index, digit in enumerate(num_str)):
            result.append(num)

    return result
