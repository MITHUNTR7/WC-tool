import os


command = input().split()

file_name = command[-1]
file_size = os.path.getsize(file_name)
print(file_size,file_name)
