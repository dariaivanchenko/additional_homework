# Вывести последнюю букву в слове
word = 'Архангельск'
print('Последняя буква в слове: ', word[len(word) - 1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
word = word.lower()
print('Количество букв "а" в слове: ', word.count('а',))

# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = 0
for i in word:
    letter = i.lower()
    if letter == "а" or letter == "я" or letter == "о" or letter == "е" or letter == "у" or letter == "ю" or letter == "ы" or letter == "и" or letter == "э" or letter == "ё":
        vowels += 1
print('Количество гласных букв в слове: ', vowels)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words_count = sentence.split()
print('Количество слов в предложении "Мы приехали в гости": ', len(words_count))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words_count = sentence.split()
# print(words_count)
for words in words_count:
    print(words[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'.split()
print('Средняя длина слова в предложении:', sum([len(words) for words in sentence]) / len(sentence))
