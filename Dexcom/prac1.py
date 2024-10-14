def lists1(str1, str2):

    dict1, dict2 = {},{}
    if len(str1) == len(str2):
        for ch in str1:
            if ch not in dict1:
                dict1[ch] = 1
            else:
                dict1[ch] += 1

        for i in range(len(str2)):
            if str2[i] not in dict2:
                dict2[str2[i]] = 1
            else:
                dict2[str2[i]] += 1

        if dict1 == dict2:
            print("Anagram")
        else:
            print("Not Anagram")

    else:
        print("Not Anagram")

lists1('test','ttes')

print('Hi Mommy')