string = input("Enter the sentence: ")
string=string.lower()
vowels = "aeiou"
vc = 0
cc = 0

for i in string:
    if i in vowels:
        vc = vc+1
    else:
        cc=cc+1

print("The number of vowels in the sentence were:", vc)
print("The number of consonents in the sentence were:", cc)
