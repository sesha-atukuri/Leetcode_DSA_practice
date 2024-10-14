def hammingDistance(x, y):
    x_bin = format(x, '032b')
    y_bin = format(y, '032b')
    min_length = min(len(x_bin), len(y_bin))
    output = 0
    for i in range(min_length):
        if x_bin[i] != y_bin[i]:
            output += 1
    return output




print(hammingDistance(1,4))