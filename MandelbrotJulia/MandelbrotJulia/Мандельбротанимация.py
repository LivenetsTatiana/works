import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import time

start_time = time.time()

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=300, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    c = p + 1j*q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T
# =============================================================================
# # инициализиация
#
#
# plt.figure(figsize=(10, 10))
# image = mandelbrot(-2.5, 1.5, 1000, -2, 2, 1000)
# plt.xticks([])
# plt.yticks([])
# plt.imshow(image, cmap='flag', interpolation='none')
# # транспонируем картинку, чтобы оси были направлены правильно
# # перед image стоит знак минус, чтобы множество Мандельброта рисовалось
# # чёрным цветом
# # параметр cmap задаёт палитру
# =============================================================================


rc('animation', html='html5')
# отображать анимацию в виде html5 video

fig = plt.figure(figsize=(10, 10))
max_frames = 100
max_zoom = 300
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

images = []
# кэш картинок

def init():
    return plt.gca()

def animate(i):
    if i > max_frames // 2:
        # фаза zoom out, можно достать картинку из кэша

        plt.imshow(images[max_frames//2-i], cmap='ocean')
        return

    p_center, q_center = -0.793191078177363, 0.16093721735804
    zoom = (i / max_frames)**3* max_zoom + 1
    scalefactor = 1 / zoom
    pmin_ = (pmin - p_center) * scalefactor + p_center
    qmin_ = (qmin - q_center) * scalefactor + q_center
    pmax_ = (pmax - p_center) * scalefactor + p_center
    qmax_ = (qmax - q_center) * scalefactor + q_center
    image = mandelbrot(pmin_, pmax_, 500, qmin_, qmax_, 500)
    plt.imshow(image, cmap='ocean')
    images.append(image)

    # добавить картинку в кэш
    return plt.gca()

ani=animation.FuncAnimation(fig, animate, init_func=init,
                               frames=max_frames, interval=1000)
mywriter = animation.FFMpegWriter(fps=5)
ani.save('mandelbrot.mp4',writer=mywriter)
print("--- %s seconds ---" % (time.time() - start_time))
