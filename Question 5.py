business_name = input("Enter your business name: ")
exclude = ['and', 'of', 'the']
words = business_name.split()
acronym = ''

for word in words:
    if word.lower() not in exclude:
        acronym += word[0].upper()

print("Acronym for",business_name,"is",acronym)