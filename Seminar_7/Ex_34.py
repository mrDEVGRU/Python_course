# Задача 34: Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов
# (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение  Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке
# *Пример:*
# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да
#     **Вывод:** Парам пам-пам


# def rhyme(words):
#     return sum(1 for i in words if i in "аеёиоуыэюя")


# text = "пара-ра-рам рам-пам-папам па-ра-па-да".lower().split()
# # text = input("Введите стих: ").lower().split()
# res = rhyme(text[0])
# if all([rhyme(i) == res for i in text]):
#     print("Парам пам-пам")
# else:
#     print("Пам парам")
