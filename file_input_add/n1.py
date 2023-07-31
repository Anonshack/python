with open('file', 'w+', encoding='UTF-8') as file:
      add = int(input("How many lines: "));
      for i in range(add):
            input1 = input("Enter string: ");
            file.write(input1 + ' ');
      # print(file)
      print('Malumot saqlandi.\n',file);
