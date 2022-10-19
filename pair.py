from allpairspy import AllPairs

n = int(input("Введите количество списков >>> "))
parameters = []
for i in range(n):
    if i == 0:
        m = "первого"
    elif i == n-1:
         m = "последнего"
    else:
        m = "следующего"

    print("Введите значения ", m, "список через пробел >> ")
    list = [_ for _ in input().split()]
    parameters.append(list)
    # list.clear()
# parameters = [
#     [i for i in input("Введите первый список через пробел >> ").split()],
#     [i for i in input("Введите второй список через пробел").split()],
#     [i for i in input("Введите третий список через пробел").split()],
#     [i for i in input("Введите четвертый список через пробел").split()],
#     [i for i in input("Введите пятый список через пробел").split()],
# ]

# print(parameters)
print("ДЛЯ ТЕСТОВ:")
for t, pairs in enumerate(AllPairs(parameters), 1):
    print(t, pairs)
