# Импорт библиотек
import pandas as pd
import matplotlib.pyplot as plt
import re
from collections import Counter
from docx import Document

# Чтение текста из документа Word

doc = Document('lion.docx') # Создание документа
# Инициализация пустой строки для накопления текста
text = '' # Для накопления текста

def paragraph(doc):
    for para in doc.paragraphs: # Перебор всех абзацев в документе
        text += para.text + ' ' # Добавление текста каждого абзацев к общей строке
    return para, text


def tex(doc):
    text = text.lower()# Приведение всего текста к нижнему регистру
    return text


# Анализ слов в тексте

# Поиск всех слов в тексте с помощью шаблона
def wor(doc):
    words = re.findall(r'\w+', text) # \w+ означает последовательность из одного или более символов букв и цифр
    return words

def count(words):
    word_counts = Counter(words)#  частота встречаемости каждого слова
    return word_counts 

# Создание таблицы со статистикой по словам

# Создание DataFrame с двумя колонками: слова и их частоты
def chast(words):
    df_words = pd.DataFrame({
    'Слово': list(word_counts.keys()),  # Список уникальных слов
    'Частота встречаемости, раз': list(word_counts.values())  # Список частот
})
    return df_words
# Добавление колонки с процентной частотой встречаемости
def sot(df_words):
    df_words['Частота встречаемости в %'] = df_words['Частота встречаемости, раз'] / df_words['Частота встречаемости, раз'].sum() * 100
    # Сохранение результатов в CSV файл
    df_words.to_csv('word_stats.csv', index=False, encoding='utf-8-sig') # Сохранение результатов в CSV 
    return df_words


# Анализ букв в тексте
def let(text):
    letters = re.findall(r'[а-яa-z]', text) # Поиск всех букв в тексте
    letter_counts = Counter(letters)# Подсчет частоты встречаемости каждой буквы
    return  letters, letter_counts

# Построение гистограммы частоты букв

plt.figure(figsize=(12, 6)) # Создание фигуры размером 12x6 
plt.bar(letter_counts.keys(), letter_counts.values()) # Построение столбчатой диаграммы: ключи - буквы, значения - частоты
plt.title('Частота встречаемости букв') # Заголовок диаграммы
plt.xlabel('Буква') # Подпись оси X
plt.ylabel('Количество') # Подпись оси Y
plt.show() # Отображение диаграммы

def main():
    para, text=paragraph(doc)
    text=tex(doc)
    words=wor(doc)
    word_counts=count(words)
    df_words=chast(words)
    df_words=sot(df_words)
    letters, letter_counts=let(text)




if __name__=='__main__':
    main()