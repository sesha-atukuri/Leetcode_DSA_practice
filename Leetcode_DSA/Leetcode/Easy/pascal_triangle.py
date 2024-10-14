def pascal_triangle(rows):
    #result = []
    if rows == 0:
        return []
    if rows == 1:
        return [[1]]
    prev_row = pascal_triangle(rows-1)
    new_row = [1]*rows
    for i in range(1,rows-1):
        new_row[i] = prev_row[-1][i-1]+prev_row[-1][i]
    prev_row.append(new_row)
    return prev_row

print(pascal_triangle(5))