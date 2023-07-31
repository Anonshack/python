def  palindrome(soz):
      soz = soz.lower()
      soz = soz.replace(" ", "")
      if soz == soz[::-1]:
            return True
      else:
            return False

if __name__ == "__main__":
      soz = input("Text: ")
      print(palindrome(soz));



# if palindrome(soz):
#       print("Palindrome")
# else:
#       print("Palindrome emas.!")
