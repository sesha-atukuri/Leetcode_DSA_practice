def isAnagram( s: str, t: str) -> bool:
    dict1, dict2 = {}, {}
    for ch in s:
        if ch not in dict1:
            dict1[ch] = 1
        else:
            dict1[ch] += 1
    for ch1 in t:
        if ch1 not in dict2:
            dict2[ch1] = 1
        else:
            dict2[ch1] += 1


    return "Anagram" if dict1 == dict2 else "Not Anagram"

print(isAnagram("anagrams",  "nagaram"))