import re


def valid_palindrome(s):
    outstr = (re.sub(r'[^A-Za-z0-9]','',s)).lower()
    if len(outstr)==0:
        return True
    for i in range(len(outstr)//2):
        if outstr[i] != outstr[len(outstr)-i-1]:
            return False

    return True



    '''dict ={}
    count = 0

    for ch in outstr:
        if ch not in dict:
            dict[ch] =1
        else:
            dict[ch] += 1
    print(dict)
    for key in dict:
        if dict[key] %2 != 0:
            if len(s) %2 != 0:
                count += 1
            else:
                return False
        else:
            count += 1
    print(count,len(dict))
    if count == len(dict):
        return True
    return False


    #return outstr'''
print(valid_palindrome("abb"))