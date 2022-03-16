import itertools
def permutation (txt):
    a = list(itertools.permutations(txt))
    for i in range(len(a)):
        print("".join(a[i]))

txt=input()
permutation(txt)