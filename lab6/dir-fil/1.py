import os
path = input("Input the path: ")
print("Directories:")
print([ name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name)) ], '\n')
print("Files:")
print([ name for name in os.listdir(path) if not os.path.isdir(os.path.join(path, name)) ], '\n')
print("Files&Directories:")
print([ name for name in os.listdir(path)])