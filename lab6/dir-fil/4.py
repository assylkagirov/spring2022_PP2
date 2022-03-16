from importlib.resources import path


pathtofile = input("Path to text file: ")
with open(pathtofile, 'r') as a:
    print('Lines Count: ', len(a.readlines()))