#string has repeated char

def repeatch(str1):
    dict1 = {}
    for ch in str1:
        if ch not in dict1:
            dict1[ch] = 1
        else:
            dict1[ch] += 1
    print(dict1)
    for ch in str1:
        if dict1[ch] > 1:
            print('yes str has repeated char')
            break
        else:
            print('No repeat char')
            break



repeatch('angrm')