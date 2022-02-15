text = str(input("Ведите текст : "))
vowels = 0
consonants = 0
for i in text:
    if i.lower() in 'aeiouy':
        if i.isalpha():
            vowels += 1
        else:
            consonants += 1
if vowels == consonants:
    print(vowels)


