N = int(input())

for i in range(N):
    if i * i < N and i != 0:
        print(str(i*i), end = " ")