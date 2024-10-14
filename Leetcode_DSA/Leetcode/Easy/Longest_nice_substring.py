def longestNiceSubstring(s):
    nice_substr = ''
    visited = ''
    for ch in s:
        if ch.islower():
            if ch.upper() in s and ch.upper() not in visited:
                nice_substr += ch
            else:
                visited = nice_substr
                nice_substr = ''
        elif ch.isupper():
            if ch.lower() in s and ch.lower() not in visited:
                nice_substr += ch
            else:
                visited = nice_substr
                nice_substr = ''
        else:
            nice_substr = ''
    return nice_substr



print(longestNiceSubstring("YazaAay"))