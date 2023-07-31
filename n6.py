def ascii_table(fayl_nomi):
    with open(fayl_nomi, "w") as fayl:
        for i in range(128):
            fayl.write(f"{i}: {chr(i)}\n")

fayl_nomi = "ascii_jadvali.txt"
ascii_table(fayl_nomi)


# def ascii_table():
#     for i in range(128):
#         print(f"{i}: {chr(i)}")
#
# ascii_table()
