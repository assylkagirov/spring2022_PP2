pathtofile1, pathtofile2 = input('Enter two file paths through space: ').split(' ')

with open(pathtofile1) as f1:
    with open(pathtofile2, "w") as f2:
        for l in f1:
            f2.write(l)