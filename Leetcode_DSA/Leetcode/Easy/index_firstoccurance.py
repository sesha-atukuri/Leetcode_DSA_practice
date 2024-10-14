def index_firstoccur(needle,haystack):
    temp = ''
    for ch in range(len(haystack)):
        if haystack[ch] == needle[0] and haystack[ch+(len(needle)-1)]==needle[len(needle)-1]:

            if haystack[ch] not in needle:
                temp = ''
            temp += haystack[ch]
            index = ch
    return index if temp == needle else -1



print(index_firstoccur("issip","mississippi"))
