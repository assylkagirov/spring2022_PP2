import os
path = input("Input the path: ")
print('E:', os.access(path, os.F_OK))
print('R:', os.access(path, os.R_OK))
print('W:', os.access(path, os.W_OK))
print('X:', os.access(path, os.X_OK))