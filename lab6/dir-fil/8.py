import os
path = input("Input the file path: ")
if os.access(path, os.F_OK) and os.access(path, os.R_OK) and os.access(path, os.W_OK):
    os.remove(path)
else:
    print("File does not exists or you do not have access to remove it")