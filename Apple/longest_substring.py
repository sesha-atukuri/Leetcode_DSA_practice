def substring(str1):
    outstr, finstr = "", ""
    for char in range(len(str1)-1):
        if str1[char] != str1[char+1]:
            outstr += str1[char]
            outstr += str1[char+1]
            #print(outstr)

        elif str1[char] == str1[char+1]:
            if len(finstr) < len(outstr):
                finstr = outstr
                outstr = ""

    print(finstr)
substring('aabbccef')
