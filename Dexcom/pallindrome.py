

def pallindrom(str):
    for i in range(len(str)):
        if str[i] == str[len(str)-i-1]:
            return 'palindrome'
        else:
            return 'not palindrome'

print(pallindrom('aabaa'))