import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()
# инициализиация

pmin, pmax, qmin, qmax = -2, 2, -2, 2
# пусть c = p + iq и p меняется в диапазоне от pmin до pmax,
# а q меняется в диапазоне от qmin до qmax

ppoints, qpoints = 200, 200
# число точек по горизонтали и вертикали

max_iterations = 300
# максимальное количество итераций

infinity_border = 10
# если ушли на это расстояние, считаем, что ушли на бесконечность

image = np.zeros((ppoints, qpoints))
# image — это двумерный массив, в котором будет записана наша картинка
# по умолчанию он заполнен нулями

#c1 = float(input ('Введите с:'))
c1=-1

for ip, p in enumerate(np.linspace(pmin, pmax, ppoints)):
    for iq, q in enumerate(np.linspace(qmin, qmax, qpoints)):
        z = p + 1j * q
        # буквой j обозначается мнимая единица: чтобы Python понимал, что речь
        # идёт о комплексном числе, а не о переменной j, мы пишем 1j
        
        c = c1
        for k in range(max_iterations):
            z = z**2 + c
            # Самая Главная Формула
            
            if abs(z) > infinity_border:
                image[ip,iq] = k
                break
plt.xticks([])
plt.yticks([])
# выключим метки на осях
plt.figure(figsize=(10, 10))
print(-image.T.max())
print(-image.T.min())
plt.imshow(-image.T, cmap='ocean')
# транспонируем картинку, чтобы оси были направлены правильно
# перед image стоит знак минус, чтобы множество Мандельброта рисовалось
# чёрным цветом
# параметр cmap задаёт палитру
print("--- %s seconds ---" % (time.time() - start_time))

