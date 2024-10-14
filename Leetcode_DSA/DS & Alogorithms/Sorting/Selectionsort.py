
def selectionsort():
    a = [2, 5, 4, 10, 7]
    #print(a)
    for i in range(len(a)):
        j = i+1
        for j in range(j, len(a)):
            print(a[i],a[j])
            if a[i] > a[j]:
                print('in if ', a[i], a[j])
                a[i], a[j] = a[j], a[i]
                print(a[i], a[j])

    return a

print(selectionsort())

