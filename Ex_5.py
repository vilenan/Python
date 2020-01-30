revenue = int(input("Введите значение выручки фирмы: "))
costs = int(input("Введите значение издержек:"))

if revenue > costs:
    print(f"Фирма работает с прибылью - {revenue - costs}")
    incom = (revenue - costs)/revenue
    print("Рентабельность выручки: ", incom)
    staff = int(input("Введите число сотрудников: "))
    staff_incom = (revenue - costs) / staff
    print("Прибыль фирмы в расчете на одного сотрудника составила: ", staff_incom)
elif revenue == costs:
    print("Фирма работает c нулевым результатом")
elif revenue < costs:
    print("Фирма работает c убытком.")