password = input("Enter your password: ")
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special = "!@#$%^&*()_-+="
check = 0

if len(password) > 8:
    check = check + 1

for i in password:
    if i.islower():
        check = check + 1
        break

for i in password:
    if i.isupper():
        check = check + 1
        break

for i in password:
    if i.isdigit():
        check = check + 1
        break

for i in password:
    if i in special:
        check = check + 1
        break


if check == 5:
    print("It is a strong password")
else:
    print("It is a weak password")