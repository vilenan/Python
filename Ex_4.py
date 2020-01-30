a = int(input("Введите целое положительное число: "))
max = a % 10
while a > 0:
    a = a // 10
    b = a % 10
    if b >= max:
        max = b
print("максимальная цифра числа: ", max)
