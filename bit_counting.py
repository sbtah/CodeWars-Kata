# Write a function that takes an integer as input, and returns the number of bits that are equal to one in the binary representation of that number.
# You can guarantee that input is non-negative.
# Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case


def count_bits(n):

    count_ones = 0
    binary = f'{n:08b}'
    new_list = list(binary)
    for x in new_list:
        if x == '1':
            count_ones += 1

    return count_ones
    
print(count_bits(1234))
