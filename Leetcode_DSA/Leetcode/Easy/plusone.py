def plusone(digits):


    for i in range(len(digits) - 1, -1, -1):
       digits[i] += 1
       if digits[i] < 10:
           return digits

       digits[i] = 0

    return [1] + digits



print(plusone([9,8,9]))
'''if i >= 0 and digits[i] == 9:
    digits[i] = 0
    if i == 0 and digits[i] == 0:
        digits = [1] + digits
elif digits[i] < 9 and digits[i + 1] == 0:
    digits[i] += 1

return digits'''

'''if 0<= digits[len(digits)-1] < 9:
            digits[len(digits) - 1] += 1
            return digits
        elif len(digits) == 1 and digits[0] == 9:
            return [1,0]

        else:
            for i in range(len(digits)-1,-1,-1):
                if i >= 0 and digits[i] == 9:
                    digits[i] = 0
                elif digits[i]< 9 and digits[i+1] == 0:
                    digits[i] +=1
                elif digits[0] == 9:
                    digits[0] += 1'''