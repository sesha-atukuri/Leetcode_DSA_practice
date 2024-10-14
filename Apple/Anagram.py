def anagram(s1,s2):
    d1, d2 = {}, {}
    for i in range(len(s1)):
        if s1[i] in d1:
            d1[s1[i]] +=1
        else:
            d1[s1[i]] = 1

    for j in range(len(s2)):
        if s2[j] in d2:
            d2[s2[j]] +=1
        else:
            d2[s2[j]] = 1

    if d1 == d2:
        print(d1, d2,'Anagram')
    else:
        print(d1, d2, 'Not Anagram')


anagram('eatt', 'ate')

