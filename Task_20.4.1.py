'''Программа получает от пользователя имя файла, открывает
этот файл в текущем каталоге, читает его и выводит два слова:
наиболее часто встречающееся из тех, что имеют размер более трех символов,
и наиболее длинное слово на английском языке.'''

# Принимаем имя файла от пользователя.
name = input("Введите имя файла: ")

# Открываем файл. Считываем текст. Убираем переводы строки. Разбиваем текст построчно на список слов.
list_of_strings = []
with open(name, 'rt', encoding="utf8") as myFile:
    for line in myFile:
        list_of_strings.append(line.replace('\n', '').split(' '))

# Объединяем построчные списки слов в список слов. Переводим слова в нижний регистр.
words = []
for i in list_of_strings:
    words.extend(i)
words = list(map(str.lower, words))

# Определяем наиболее часто встречающееся слово из тех, что имеют размер более трех символов.
frequent_word = words[0]
for word in words:
    if len(word) > 3:
        count = words.count(word)
        if count >= words.count(frequent_word):
            frequent_word = word
print("Наиболее часто встречающееся слово размера более трех символов: ", frequent_word)

alpha_eng = 'abcdefghijklmnopqrstuvwxyz'
eng_words = []


# Функция определяет, состоит ли слово из английских букв.
def eng(word):
    for char in word:
        if char in alpha_eng:
            return True
        else:
            return False


#  Если слово состоит из английских букв, добавляем слово в список английских слов.
for word in words:
    if eng(word):
        eng_words.append(word)

#  Ищем наиболее длинное слово на английском языке.
longest = eng_words[0]
for word in eng_words:
    if len(word) >= len(longest):
        longest = word
print("Наиболее длинное слово на английском языке: ", longest)
