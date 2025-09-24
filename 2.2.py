
sentence = input("Введите строку, разделённую точками с запятой: ")

# Разделяем строку по символу ';'
words = sentence.split(';')

# Находим самое длинное слово
longest_word = max(words, key=len)

# Выводим результат
print("Самое длинное слово:", longest_word)
