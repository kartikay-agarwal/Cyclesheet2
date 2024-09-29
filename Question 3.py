email = input("Enter your email address: ")
acount = 0
fcount = 0
parts = []
valid = 0

if email.startswith('@') or email.startswith('.'):
    print("Invalid Email Address")
else:
    valid = valid + 1

    for ch in email:
        if ch == "@":
            acount = acount+1

    if acount > 1:
        print("Invalid Email Address")
    else:
        parts = email.split('@')
        valid = valid + 1

        for c in parts[0]:
            if not (c.isalnum() or c == '_' or c == '.'):
                print("Invalid Email Address")
                break
            else:
                valid = valid + 1
                break

        for ch in parts[1]:
            if ch == '.':
                fcount = fcount + 1

        if fcount == 0:
            print("Invalid Email Address")
        else:
            valid = valid + 1

if valid == 4:
    print("Valid Email Address")