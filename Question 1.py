sentence= input("Enter a sentence or word: ")
lower = sentence.lower()
filter = []

for char in lower:
    if char.isalpha():
        filter.append(char)

clean_str = ''.join(filter)

if clean_str == clean_str[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
