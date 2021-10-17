from random import randint

numbers = [-6, 7, -2, -6, 6, 9, 1, -4, 0, -8, -4, 10, 2, 6, 10, -6, 4, -3, 0, 3]
print(numbers)
print(len(numbers))
for i in range(len(numbers) - 1):
    for j in range(len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print(numbers)