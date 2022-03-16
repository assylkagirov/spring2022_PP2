def solve(numheads, numlegs):
    numr = (numlegs-2*numheads)/2
    numc = numheads - numr
    return int(numr), int(numc)

x, c = map(int, input().split())
print(solve(x,c))