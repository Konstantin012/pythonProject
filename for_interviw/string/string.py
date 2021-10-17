# сколько раз символ встречается в строке
string = 'Python Software Foundation'
print(string.count('o'))

# Нарисовать треугольник заданной размерности. Пример для размера 6:
# *
# **
# ***
# ****
# *****
# ******

def create_symb():
    a = "*"
    for i in range (0,7):
        print(a*i)

create_symb()

def create_symb1():
    a = "*"
    for i in range (0,15,3):
        print(a*i)

create_symb1()

