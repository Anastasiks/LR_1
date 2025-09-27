
# 1
# import math
# a = int(input())
# b = float(input())
# print("сумма = ", a + b, type(a + b))
# print("разность = ", a - b, type(a - b))
# print("произведение = ", a * b, type(a * b))
# print("деления = ", a / b, type(a / b))
# print("площадь круга = ", round((math.pi * 5**2),2),  type(math.pi * 5**2))

# 2
# text = " Hello, Python! "
# text = text.strip()
# print(text.strip())
# print(text.replace("!", "?"))
# print(text.upper())
# text = text.lower()
# print(text)

# 3
# numbers = [7, 2, 5]
# numbers.append(4)
# print("добавлено число 4", numbers)
# numbers.insert(1, 10)
# print("добавлено число 10 на вторую позицию", numbers)
# numbers.extend([1, 1, 1])
# print("Расширен список элементами [1, 1, 1] ", numbers)
# numbers.remove(7)
# print("удалено число 7", numbers)
# pop = numbers[-1]
# numbers.pop()
# print("удален последний элемент списка", numbers)
# numbers.sort()
# print("отсортирован список", numbers)
# numbers.reverse()
# print("разаернула список", numbers)
# print("2 встречается", numbers.count(2), "раз")
# print("index 1:", numbers.index(1))
# copy = numbers[::]
# decopy = numbers[::]
# numbers.clear()
# print(copy, decopy, numbers)

# 4
# t = (1, 2, 3)
# # t[1] = 100 - не работает потомму что кортеж - неизменяемый
# t2 = t + (4, 5)
# print("Соединила кортеж t с другим кортежем:", t2)
# print("количество троек в t2 =", t2.count(3))
# print("ииндекс элемента 4 = ", t2.index(4))
# print(t)

# 5
# values = [3, 1, 3, 2, 1, 5, 2]
# unique_values = set(values)
# print("кол-во уникальных элементов:", len(unique_values))
# print("множество:", unique_values)
# other = {2, 4, 5}
# print("пересечение двух множеств", unique_values & other)
# print("объединение двух множеств", unique_values | other)
# print("разность unique_values - other", unique_values - other)
# print("разность other - unique_values", other - unique_values)

# 6
# scores = {"Alice": 85, "Bob": 90}
# scores["Charlie"] = 78
# print("добавили новый пункт", scores)
# scores["Bob"] = 95
# print("изменили балл  Боба", scores)
# print("кол-во баллов у Дэйва", scores.get("Dave"))
# print("кол-во баллов у Алисы", scores.get("Alise"))
# scores.pop("Alice")
# print("удалили студента", scores)
# print("итог:", scores)
# print("длинна итога:", len(scores))
# print("ключи", scores.keys())
# print("значение", scores.values())

# 7
text = """
    Python is a powerful programming language. 
    It is used in data science, web development, automation, and many other fields!
    PYTHON is easy to learn, yet very versatile.
"""
t = text.strip().lower()
t = t.replace("!", ".")
sentences = [s.strip() for s in t.split(".") if s.strip()]
print("Предложения:", sentences)
first = sentences[0]
words = first.split()
print("Слова первого предложения:", words)
print("Кол-во 'python':", words.count("python"))
print("startswith('python'):", first.startswith("python"))
print("endswith('language'):", first.endswith("language"))
print("Общее кол-во символов:", len(t))
print("Кол-во букв 'a':", t.count("a"))
print("Индекс слова 'data':", t.find("data"))

words_all = t.split()
print("Через '-':", "-".join(words_all))
freq = {}

freq = {}
for w in words_all:
    freq[w] = freq.get(w, 0) + 1
print("Частоты слов:", freq)
import string
def clean_text(txt):
    txt = txt.lower().strip()
    allowed = string.ascii_lowercase + " "
    cleaned = "".join(ch if ch in allowed else " " for ch in txt)
    return " ".join(cleaned.split())

print("Очищенный текст:", clean_text(text))

