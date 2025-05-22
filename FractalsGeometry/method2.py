from PIL import Image, ImageDraw #open images
import matplotlib.pyplot as plt #create plots
import numpy as np #array processing
from sklearn.linear_model import LinearRegression #regression
from math import log, sqrt #maths function

def FractalCount(a, n):# n - кол-во блоков
    t = transp(a)
    count = 0
    net = 5 # сетка 5*5
    size = 100 # размер одной клетки
    part = n % net
    whole = n // net
    #print(whole, " , ", part)
    if (whole == 0 or (whole == 1 and part == 0)): # прямоугольники, когда идем по первой строке
        count = intersections(a[0][0:(size*part-1)])+intersections(a[size-1][0:(size*part-1)])
        +intersections(t[0][1:(size-1)]) 
        + intersections(t[(size*part-1)][1:(size-1)])
        #print("case1")
        
    elif (part == 0): # прямоугольники, в случае захвата нескольких строк
        count = intersections(a[0][0:(size*net-1)])+intersections(a[whole*size-1][0:(size*net-1)])
        +intersections(t[0][1:whole*size-1]) + intersections(t[size*net-1][1:whole*size-1])
        #print("case2")
    else: # г-образные фигуры
        count = intersections(a[0][0:(size*net-1)])
        +intersections(a[(whole+1)*size-1][0:(size*part-1)]) + intersections(a[(whole)*size-1][(size*part-1):(size*net-1)])
        +intersections(t[0][1:(whole+1)*size-1]) + intersections(t[(size*part-1)][(whole*size):(whole+1)*size-1])
        +intersections(t[size*net-1][1:(whole)*size-1])
        #print("case3")
    return count
       
def intersections(a): #если после черного пикселя идет белый, то это конец пересечения
    count = 0
    #print(' ', len(a), ' ')

    for i in range(len(a)-1):
        if (a[i]==100).all() and (a[i+1]==255).all():
            count+=1
    return count

def transp(a):
    a0 = np.zeros(shape=(500, 500, 3))
    for x in range(a.shape[0]):
        for y in range(a.shape[1]):
            a0[y][x] = a[x][y]
    return a0
     
def Y(a0, n):
    y0 = FractalCount(a0, n) 
    if (y0>0): 
        return y0
    else: return 0
    
image = Image.open("карты/all_volga_4.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	



#im_rotate = image.rotate(-90)
#im_rotate.save('guido_90.jpg', quality=100)
#image.close()
#image = im_rotate
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
x = np.array([sqrt(i) for i in range(1, 5)])
x = np.append(x, sqrt(10))
y = np.array([Y(a, i) for i in range(1, 5)])
y = np.append(y, Y(a, 10))

#x = np.array([log(sqrt(i+1)) for i in range(5)]).reshape(-1, 1)
#y = np.array([Y(a, i+1) for i in range(5)])
x_log = (np.log(x)).reshape(-1, 1)
y_log = np.log(y)
model = LinearRegression().fit(x_log, y_log)
level = 'green'
#if (model.coef_[0]>=1.5): level = 'orange'
#if (model.coef_[0]>=1.65): level = 'red'
a = model.coef_[0]/2+1
plt.text(0, 0, '%.2f' % a, fontsize=10,
             color = level, rotation = 30)
#print(model.coef_)
plt.show()
fig, axs = plt.subplots()
plt.loglog(x, y)
#plt.semilogx(x, y) 
