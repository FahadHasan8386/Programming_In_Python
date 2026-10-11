ch = input("Enter a Character : ")

if ch.lower() in "aeiou" and len(ch) == 1:
    print("The Character is vowel")
else:
    print("The Character is not vowel")