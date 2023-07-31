input_str = input("Str yoki Float Kiriting: ")
sonlar = input_str.split()

stringlar = []
floatlar = []

for son in sonlar:
    try:
        float_son = float(son)
        floatlar.append(float_son)
    except ValueError:
        stringlar.append(son)


print("Stringlar:", stringlar)
print("Floatlar:", floatlar)
