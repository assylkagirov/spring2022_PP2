def calculating(det, inputn, val, dictc):
    while det < len(inputn):
        for i in range(10):
            if dictc[i] == inputn[det] + inputn[det + 1] + inputn[det + 2]:
                val.append(i)
        det = det + 3
    return val

def calc_val(val, valreal):
    for i in range(len(val)):
        valreal = valreal + str(val[i])
    return valreal
dict = ['ZER', 'ONE', 'TWO', 'THR', 'FOU', 'FIV', 'SIX', 'SEV', 'EIG', 'NIN']
input1 = list(input())
val1 = []
val2 = []
input2 = []
input3 = []
input4 = []
for i in range(len(input1)):
    if input1[i] == '+':
        del input1[i]
        for l in range(i):
            input2.append(input1[l])
        for l in range(len(input1) - i):
            input3.append(input1[len(input1) - 1 - l])
        break
det1 = 0
det2 = 0
input3.reverse()
val1 = calculating(det1, input2, val1, dict)
val2 = calculating(det2, input3, val2, dict)
valreal1 = ""
valreal2 = ""
valreal1 = calc_val(val1, valreal1)
valreal2 = calc_val(val2, valreal2)
valrealfinal = ""
valfinal = list(str(int(valreal1) + int(valreal2)))
for i in range(len(valfinal)):
    valrealfinal = valrealfinal + dict[int(valfinal[i])]
print(valrealfinal)