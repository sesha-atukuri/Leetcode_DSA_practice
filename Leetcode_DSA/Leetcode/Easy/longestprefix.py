def longest_prefix(strs):
    prefix = strs[0]
    for string in strs[1:]:
        while string.find(prefix)!=0:
            prefix = prefix[:-1]
            if prefix == "":
                break
    return prefix

print(longest_prefix(["flower","flow","flight"]))