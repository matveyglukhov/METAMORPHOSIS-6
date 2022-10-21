import numpy as np
while True:
    try:
        b_number = int(input("Количество критериев "))
        break
    except ValueError:
        print('Неверный ввод')
# Создание матрицы
b_ma = np.eye(b_number)
# Заполнение матрицы коэффициентами
a = 1
for i in range(a, b_number+1):
    for j in range(a+1, b_number+1):
        while True:
            try:
                #Заполняем каждый элемент строки матрицы
                b_ma[i-1][j-1] = round(float(input('Введите сравнение К{0}-К{1}: '.format(i, j))), 3)
                break
            except ValueError:
                print('Неверный ввод')
        # Заполнение ячеек для обратного соотношения
        b_ma[j-1][i-1] = round(b_ma[i-1][j-1]**(-1), 2)
    a += 1
# Создание сумм строк
comp_l = [round(sum(j),2) for j in b_ma]
out_l = [round(n/sum(comp_l), 2) for n in comp_l]
if (sum(out_l)) != 1.0:
    index = out_l.index(max(out_l))
    k = (sum(out_l)) - 1.0
    out_l[index] -= k
print('Весовые коэффициенты')
for ind in out_l:
    print(ind, end=' ')