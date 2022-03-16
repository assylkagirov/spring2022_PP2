compare = {}
max = 0
listt = []
x = int(input())

for i in range(x):
    s = input()
    s = s.split()
    if s[0] in compare:
        compare[s[0]] += int(s[1])
        if max < compare[s[0]]:
            max = compare[s[0]]
    else:
        compare[s[0]] = int(s[1])
        listt.append(s[0])
        if max < compare[s[0]]:
            max = compare[s[0]]
listt = sorted(listt)

for i in listt:
    if compare[i]==max:
        print(i,'is lucky!')
    else:
        print(i, 'has to receive {} tenge' .format(max-compare[i]))