
with open('fayl.txt', 'a') as file:
      file.write("This is my file.");
      print(file);


import os

old_file = 'umar.txt';
new_file = 'add.txt';

os.rename(old_file,new_file)