import os
path = input('Input the path: ')
exist = os.path.exists(path)
print(exist, '\n')
if exist:
    print("File name of the path:")
    print(os.path.basename(path), '\n')
    print("Directory Portion:")
    print(os.path.dirname(path))