n = int(input())
if n >= 1 or n >= 99:
    arr = [[0] * n for i in range(n)]
    cmd1 = 0
    cmd2 = 0
    for i in range(n):
        for j in range(n):
            if i == 0:
                arr[0][j] = cmd1
                cmd1 += 1
            if j == 0:
                arr[i][0] = cmd2
                cmd2 += 1
            if i == j:
                arr[i][j] = i * j
            print(arr[i][j], end = ' ')
        print()
    
else:
    print("0")