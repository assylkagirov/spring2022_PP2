anylist = ['1', '2', '3']

pathtofile = input('Where to write?: ')

with open(pathtofile, 'w') as a:
    for i in anylist:
        a.write("%s\n" % i)