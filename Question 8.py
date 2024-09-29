string = input("Enter a sentence: ")
words = string.lower().split(" ")
word = {}

string=string.lower()
vowels = "aeiou"
vc = 0
cc = 0

for i in words:
    if i not in word:
        word[i] = 1
    else:
        word[i] +=1

for i in string:
    if i in vowels:
        vc = vc+1
    else:
        cc=cc+1


for words, count in word.items():
    print(words,":", count)

print("The number of vowels in the sentence were:", vc)
print("The number of consonents in the sentence were:", cc)
