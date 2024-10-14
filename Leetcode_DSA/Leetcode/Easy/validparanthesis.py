def isvalid(s:str) ->bool:
    characters = {')': '(', '}': '{', ']': '['}
    output = []
    for ch in s:
        if ch in characters:
            if not output or characters[ch] != output.pop():
                return False
        else:
            output.append(ch)

    return not output

print(isvalid("]"))