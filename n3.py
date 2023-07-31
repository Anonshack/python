def countLetters(soz):
      katta_hariflar = 0
      kichik_hariflar = 0

      for harf in soz:
            if harf.isupper():
                  katta_hariflar += 1
            elif harf.islower():
                  kichik_hariflar += 1

      return katta_hariflar, kichik_hariflar
soz = input("Istalgan so'zni kiriting: ")
katta, kichik = countLetters(soz)
print("Katta hariflar soni:", katta)
print("Kichik hariflar soni:", kichik)
