#Generate ALL possible subsets of a given set.
# The set is given in the form of a string s containing distinct lowercase characters 'a' - 'z'.

result = []
def subset(s):

    helper(s,0,'')
    return result

def helper(s,i,prestr):
    if i == len(s):
        return result.append(prestr)

    helper(s,i+1,prestr)
    helper(s,i+1,prestr+s[i])


print(subset('xy'))

