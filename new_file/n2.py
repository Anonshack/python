import os

dosya_ad1 = "fayl.txt"

# exisits() - Mavjud
if os.path.exists(dosya_ad1):
    os.remove(dosya_ad1)
    print(f"{dosya_ad1} fayl bor.")
else:
    print(f"{dosya_ad1} bunday file yoq.")
