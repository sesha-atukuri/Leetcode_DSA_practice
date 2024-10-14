def reverse_bits(n):
    reversed_num = 0

    # Iterate over all 32 bits of the given number
    for i in range(32):

        bit = (n >> i) & 1

        reversed_num = reversed_num | (bit << 31 - i)

    # Return the reversed number
    return reversed_num

str = 0o0000010100101000001111010011100

print(reverse_bits(str))