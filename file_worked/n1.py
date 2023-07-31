fayilnomi = 'new_file.txt'
# ism = "Kozimjonov Qudratbekh "
# tyil = 2005
#
# with open(fayilnomi, 'w') as fayl:
#       fayl.write(ism+'\n');
#       fayl.write(str(tyil))



# append()
tyil = 1998;
with open('new_file.txt', 'a') as file:
      file.write("Saud Abdlvahed ");
      file.write(str(tyil));