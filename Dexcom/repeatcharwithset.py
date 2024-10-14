str = 'abgg'
setsam = set()

for ch in str:
    if ch in setsam:
        print(ch)

    else:
        setsam.add(ch)

print(setsam)