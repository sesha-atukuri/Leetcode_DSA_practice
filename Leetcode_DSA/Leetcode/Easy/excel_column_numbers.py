def excel_column_num(col_name):
    num = 1
    dict = {}
    res = 0
    for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        dict[ch] = num
        num = num+1
    for i in col_name:
        res = res*26 + dict[i]

    return res


print(excel_column_num("AA"))



