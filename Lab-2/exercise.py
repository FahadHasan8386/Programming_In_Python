age = 22
print("Your Age is : " , age)

if age >= 18:
    print("You are adult")
else:
    print("You are not adult")

marks = int(input("Enter your Marks : "))

if marks % 2 == 0 :
    print("Number is even")
else:
    print("Number is odd .")


email = input("Enter your email: ")

if "@gmail.com" in email :
    print("This is a gmail")
elif email == "":
    print("Email is not empty")
else:
    print("Unknown users")

name = "Fahad Hasan"

print(name.upper())
print(name.lower())
print(name.title())
print(name.replace("Fahad", "Md Fahad"))

print(len(name))