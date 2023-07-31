import os
file_path = 'file_to_check.txt'

if os.path.exists(file_path):
    print(f"The file '{file_path}' exists.")
else:
    print(f"The file '{file_path}' does not exist.")

with open('file_to_check.txt', 'r+') as file:
      add = file.read()
      file.write(' Assalomu alaykum')
print(add)