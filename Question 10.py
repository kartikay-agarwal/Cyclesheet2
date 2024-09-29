username = input("Enter a username: ")
valid = 0

if len(username) < 5 or len(username) > 12:
    print("Username should be between 5 and 12 characters.")
else:
    valid = valid + 1

if not username[0].isalpha():
    print("Username should start with an alphabetic character.")
else:
    valid = valid + 1

for char in username:
    if not (char.isalnum() or char == '_'):
        print("Username can only contain letters, digits, and underscores (_).")
    else:
        valid = valid + 1

if valid == 3:
    print("Valid Username")
else:
    print(valid)
