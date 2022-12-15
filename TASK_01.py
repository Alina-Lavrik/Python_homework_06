# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# ' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'

# Вариант 1
# stroka = input("Введите текст через пробел: ")
'''stroka = 'абвгд гдежз жзе абв ыопыпт'
print(f'Текущий текст: {stroka}')
find_stroka = "абв"
stroka1 = [i for i in stroka.split() if find_stroka not in i]
print(f'Новый текст: {" ".join(stroka1)}')'''

# Вариант 2
del_st = lambda x, y: " ".join([i for i in x.split() if y not in i])

print(del_st('абвгд гдежз жзе абв  ыопыпт', 'абв'))
