import pickle

with open('info.txt', 'rb') as file:
      talaba1 = pickle.load(file)
      talaba2 = pickle.load(file);

print(talaba1)
print(talaba2)