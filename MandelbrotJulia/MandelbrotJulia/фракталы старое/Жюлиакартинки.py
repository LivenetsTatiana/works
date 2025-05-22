import numpy as np
import matplotlib.pyplot as plt
import time

start_time = time.time()

def julia(pmin, pmax, ppoints, qmin, qmax, qpoints,
               max_iterations=300, infinity_border=10):
    image = np.zeros((ppoints, qpoints))
    p, q = np.mgrid[pmin:pmax:(ppoints*1j), qmin:qmax:(qpoints*1j)]
    z = p + 1j*q
    c = -(1-0.0*1j)*np.ones_like(z)
    for k in range(max_iterations):
        z = z**2 + c
        mask = (np.abs(z) > infinity_border) & (image == 0)
        image[mask] = k
        z[mask] = np.nan
    return -image.T

fig = plt.figure(figsize=(30, 30))
pmin, pmax, qmin, qmax = -2, 2, -2, 2

def zoomjulia(i):
    p_center, q_center = -0.6, 0
    scalefactor = 1 / i
    pmin_ = (pmin - p_center) * scalefactor + p_center
    qmin_ = (qmin - q_center) * scalefactor + q_center
    pmax_ = (pmax - p_center) * scalefactor + p_center
    qmax_ = (qmax - q_center) * scalefactor + q_center
    image = julia(pmin_, pmax_, 500, qmin_, qmax_, 500)
    plt.imshow(image, cmap='ocean',extent=(pmin_, pmax_, qmin_, qmax_), vmin=-26, vmax=0)
    plt.xticks(fontsize=30)
    plt.yticks(fontsize=30)
    plt.savefig('jul.png')

print("Input zoom")
#z=int(input("z="))
zoomjulia(1)
