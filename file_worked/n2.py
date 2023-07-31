import pickle

talaba1 = {'ism':'hasan', 'familiya':'Kozijonov', 't_yil':2005, 'kurs':2};
talaba2 = {'ism':'Umar', 'familiya':'Olimov', 't_yil':2000, 'kurs':3};

with open('info.txt', 'rb') as file:
      pickle.dump(talaba1, file);
      pickle.dump(talaba2, file);
