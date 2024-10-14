str = 'test'
dict = {}
for ch in str:
    if ch not in dict:
        dict[ch] = 1
    else:
        print('first repeated char', ch)
        break