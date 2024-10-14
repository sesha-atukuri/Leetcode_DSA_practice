def reversestring(s):
    for ch in range(len(s) // 2):
        s[ch], s[len(s) - 1 - ch] = s[len(s) - 1 - ch], s[ch]
    print(s)

reversestring(["h","e","l","l","o"])