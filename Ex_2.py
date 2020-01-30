t = int(input("Введите время в секундах: "))
chas = t // 3600
min = t % 3600 // 60
sek = t % 3600 % 60
print(f"Вы ввели время: {chas} : {min} : {sek} ")