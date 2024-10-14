# Given a base a and an exponent b. Your task is to find ab. The value could be large enough.
# So, calculate ab % 1000000007.

def power(a,b):
    result = 1
    mod = 1000000007
    poweroftwo = a%mod

    while b!=0:
        if b%2 == 1:
            result = (result * poweroftwo)%mod
            print(b,'inside odd number con')

        poweroftwo = (poweroftwo*poweroftwo)%mod
        b = b//2
        print(result)
    return result


print(power(3,4))