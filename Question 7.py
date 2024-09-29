string = input("Enter a sentence: ")
words = string.lower().split(" ")
word = {}

for i in words:
    if i not in word:
        word[i] = 1
    else:
        word[i] +=1

for words, count in word.items():
    print(words,":", count)
