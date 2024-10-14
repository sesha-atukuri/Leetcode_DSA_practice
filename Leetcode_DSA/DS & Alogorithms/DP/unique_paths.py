def unique_paths(n,m):


    tab_2d = [[0 for _ in range(m+1)]for _ in range(n+1)]


    for i in range(1,n+1):
        for j in range(1,m+1):
            if i == 1 and j == 1:
                tab_2d[i][j] = 1
            elif i == 1:
                tab_2d[i][j] += tab_2d[i][j-1]
            elif j == 1:
                tab_2d[i][j] += tab_2d[i-1][j]
            else:
                tab_2d[i][j] = tab_2d[i][j-1]+tab_2d[i-1][j]
            tab_2d[i][j] %= 10**9+7
    return tab_2d[n][m]


print(unique_paths(3,2))