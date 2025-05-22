import numpy as np
import matplotlib.pyplot as plt
import time
from PIL import Image

start_time = time.time()

def mandelbrot(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=300, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    c = p + 1j*q
    z = np.zeros_like(c)
    for k in range(max_iterations):
        z = z**10 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

fig = plt.figure(figsize=(30, 30))
pmin, pmax, qmin, qmax = -2.5, 1.5, -2, 2

def zoom(i, x0, y0):
    p_center, q_center = x0, y0
    scalefactor = 1 / i
    pmin_ = (pmin - p_center) * scalefactor + p_center
    qmin_ = (qmin - q_center) * scalefactor + q_center
    pmax_ = (pmax - p_center) * scalefactor + p_center
    qmax_ = (qmax - q_center) * scalefactor + q_center
    image = mandelbrot(pmin_, pmax_, 500, qmin_, qmax_, 500)

    plt.imshow(image, cmap='ocean',extent=(pmin_, pmax_, qmin_, qmax_))
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.savefig('manthsttghs.png')

def resize(width, height, image):
    img = Image.open(image)
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    resized_img.save(image)


# print("Input zoom")
# z=int(input("z="))
x=-0.793191078177363
y=0.16093721735804
z=1

zoom(z, x, y)

# resize(int(200.5), int(200.5), 'image123.png')
