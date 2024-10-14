def roman_integer(str):

    dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    output = 0

    for i in range(len(str)):
        if i < len(str)-1 and dict[str[i]] < dict[str[i+1]]:
            output -= dict[str[i]]

        else:
            output += dict[str[i]]

    print(output)

roman_integer("MCMXCIV")