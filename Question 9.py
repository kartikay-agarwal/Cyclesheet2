sentence = input("Enter a sentence: ")

words = sentence.split(' ')
reversed_words = words[::-1]
reversed_sentence = ' '.join(reversed_words)
    
print("Result: ",reversed_sentence)