# 1-usul
# add = open('file.txt', 'r')
# clay = add.read();
# print(clay)
#
# add.close()



#2-usul
# with open('file.txt', 'r') as file:
#       add = file.read()
#       print(add)


#Malumot add
# with open('file.txt', 'a') as file:
#       file.write("This is my file");
#       print(file)



#File nomini o'zgartirish
# import os
#
# old_file = 'umar.txt';
# new_file = 'new_file_4';
# os.rename(old_file, new_file)


# 1-usul
import os
# clay = 'www1.txt';
# if os.path.exists(clay):
#       print(f"{clay} File bor");
# else:
#       print(f"{clay} bunday file yoq.!");



#2-usul
# if os.path.exists('sat'):
#       os.remove('set');
# else:
#       print('There is not this file...!');



# with open('text.txt', 'r') as file:
#       add = file.read();
#       for i in add:
#             if i == ' ':
#                   i.replace('', ' ');
#             print(i, end=' ');
# print('\n', add);


def my_file_work(soz, theme):
    with open(theme, 'r') as clay:
        series = 0
        for satir in clay:
            series += 1
            if soz in satir:
                return series
    return -1

soz = input("So'znig kiriting: ")
input1 = input("File nomini kiriting: ")

add = my_file_work(soz, input1)

if add == -1:
    print(f"'{soz}' so'zi faylda topilmadi.")
else:
    print(f"'{soz}' so'zi faylda {add}-qatorda topildi.")

