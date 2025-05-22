from PIL import Image, ImageDraw #open images
import matplotlib.pyplot as plt #create plots
import numpy as np #array processing
from sklearn.linear_model import LinearRegression #regression
from math import log #maths function

def FractalCount(a, n):#n*n - number of blocks
    count = 0
    size = 100//n
    n1, n2 = -size, 0
    
    for k in range(n*n): #проход по всем маленьким массивам большого массива
        if k % n== 0: 
            n1+=size
            n2=0
        else: 
            n2+=size
        isblack = False
        for i in range(size): #гуляем по маленькому массиву
            if (isblack): break
            for j in range(size):
                if (a[i+n1][j+n2]==100).all():
                    count+=1
                    isblack = True
                    break
    return count
            
def Y(a0, n):
    y0 = FractalCount(a0, n) 
    if (y0>0): 
        return log(y0)
    else: return 0
    
image = Image.open("карты/Волга_Дельта.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	

pix = image.load() #Выгружаем значения пикселей.

factor = 10
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
#print(a)
n1, n2 = -500, 0
a0 = np.zeros(shape=(500, 500, 3))
for k in range(1): #проход по всем маленьким массивам большого массива
    for i in range(500): #гуляем по маленькому массиву
        for j in range(500):
            a0[i, j] = a[i][j]
    #можно обрабатывать а0(клетку)
    #print(k, n1, n2)
    
    x = np.array([log(10), log(20), log(25), log(50), log(100)]).reshape(-1, 1)
    y = np.array([Y(a0, 5), Y(a0, 20), Y(a0, 25), Y(a0, 50), Y(a0, 100)])
    #print(y)
    model = LinearRegression().fit(x, y)
    level = 'green'
    if (model.coef_[0]>=1.5): level = 'orange'
    if (model.coef_[0]>=1.65): level = 'red'
    
    plt.text(n2, n1+500, '%.2f' % model.coef_[0], fontsize=10,
             color = level, rotation = 30)
    #print(model.coef_)
plt.show()
fig, axs = plt.subplots()
plt.plot(x, y)
