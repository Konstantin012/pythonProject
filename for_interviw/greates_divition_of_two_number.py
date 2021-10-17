def divide(a: int, b: int):
    for i in range(1, a):
        if a % i == 0 and b % i == 0:
            print(i)

divide(36, 66)

a = 50
b = 130

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a

print(a + b)




a = 99
b = 66

while a != b:
    if a > b:
        a = a - b
    else:
        b = b - a

print(a)
