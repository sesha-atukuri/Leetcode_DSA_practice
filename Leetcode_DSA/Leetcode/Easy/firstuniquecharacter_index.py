def first_uniquechar(s):
    ans = {}

    for ch in range(len(s)):
        if s[ch] not in ans:
            ans[s[ch]] = 1
        else:
            ans[s[ch]] += 1
    print(ans)
    for index in range(len(s)):
        print(s[index])
        if ans[s[index]] == 1:
            return index






print(first_uniquechar("loveleetcode"))