num = int (input ("Enter a number: "))
if num == 1:
    print(num, "Tub Son emas !")
elif num > 1:
    for i in range (2, num):
        if (num % i) == 0:
            print(num, "Tub Son emas !")
            break
    else:
        print(num, "Tub Son")
else:
    print(num, "Tub Son emas !")
