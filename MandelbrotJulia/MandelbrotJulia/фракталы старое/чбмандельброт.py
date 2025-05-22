import numpy as np
import matplotlib.pyplot as plt

pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2
# пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
# а q меняется в диапазоне от qmin до qmax

ppoints, qpoints = 100, 100
# число точек по горизонтали и вертикали

max_iterations = 300
# максимальное количество итераций

infinity_border = 4
# если ушли на это расстояние, считаем, что ушли на бесконечность

#image = np.zeros((ppoints, qpoints))
image = np.ones((ppoints, qpoints))
# image — это двумерный массив, в котором будет записана наша картинка
# по умолчанию он заполнен единицами

for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):#эта штука делает из двумерного массива одномерный и пробегается по оси х(действительная часть)
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):#пробег по одномерному массиву по у(мнимая часть)
        c = p + 1j * q
        # буквой 1j обозначается мнимая единица: чтобы Python понимал, что речь

        z = 0
        for k in range(max_iterations):
            z = z**2 + c
            # Самая Главная Формула

            if abs(z) > infinity_border:
                # если z достаточно большое, считаем, что последовательость
                # ушла на бесконечность
                # или уйдёт
                # можно доказать, что infinity_border можно взять равным 4

                image[ip,iq] = 0
                # находимся вне M: отметить точку как белую
                break
print(image)
# plt.xticks([])
# plt.yticks([])
# выключим метки на осях

# plt.imshow(-image.T, cmap='Greys')
# транспонируем картинку, чтобы оси были направлены правильно
# перед image стоит знак минус, чтобы множество Мандельброта рисовалось
# чёрным цветом
