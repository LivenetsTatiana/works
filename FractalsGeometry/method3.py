from PIL import Image, ImageDraw #open images
import matplotlib.pyplot as plt #create plots
import numpy as np #array processing
from sklearn.linear_model import LinearRegression #regression
from math import log, sqrt, cos #maths function

def FractalCount(a, X0, Y0, R):# n - кол-во блоков
    n = 0 #number of intersections
    for i in range(270, 360):
        y = Y0 + R*cos(i)
        x = X0+ R*cos(i)
        x=int(x)
        y=int(y)
        if (a[x][y]==100).all():
            n=n+1
    return n
    
def Y(a0, X0, Y0, R):
    y0 = FractalCount(a0, X0, Y0, R) 
    if (y0>0): 
        return y0
    else: return 0
    
image = Image.open("карты/all_volga_4.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	

pix = image.load() #Выгружаем значения пикселей.
factor = 100
for i in range(width):
	for j in range(height):
			a = pix[i, j][0]
			b = pix[i, j][1]
			c = pix[i, j][2]
			S = a + b + c
			if (S > (((255 + factor) // 2) * 3)):
				a, b, c = 255, 255, 255#white
			else:
				a, b, c = 100, 100, 100#black
			draw.point((i, j), (a, b, c))
#image.save("ans.jpg", "JPEG")
fig, axs = plt.subplots(figsize=(9,9))
plt.imshow(image)
axs.grid()
#plt.text(100, 100, 23, fontsize=10)

del draw

a = np.asarray(image)
#x = np.array([log(sqrt(i)) for i in range(4, 17)]).reshape(-1, 1)
#y = np.array([Y(a, 100, 0, i*20) for i in range(4, 17)])

x = np.array([i*30 for i in range(1, 6)]).reshape(-1, 1)
y = np.array([Y(a, 200, 200, i*10) for i in range(1, 6)])
x_log = (np.log(x)).reshape(-1, 1)
y_log = np.log(y)
#x = np.array([log(sqrt(i+1)) for i in range(5)]).reshape(-1, 1)
#y = np.array([Y(a, i+1) for i in range(5)])
model = LinearRegression().fit(x_log, y_log)
level = 'green'
if (model.coef_[0]>=1.5): level = 'orange'
if (model.coef_[0]>=1.65): level = 'red'
a = model.coef_[0]/2+1
plt.text(0, 0, '%.2f' % a, fontsize=10,
             color = level, rotation = 30)
    #print(model.coef_)
plt.show()
fig, axs = plt.subplots()
#plt.plot(x, y)
plt.loglog(x, y)