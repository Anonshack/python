with open('umar.txt', 'r') as file:
      add = file.read()
      for i in add:
            if i == ' ':
                  i.replace(' ', '')
            print(i, end=' ')
print('\n',add)
