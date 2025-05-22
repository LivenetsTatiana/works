import matplotlib.pyplot as plt # create plots
import numpy             as np  # array processing

from sklearn.linear_model import LinearRegression # regression
from math                 import log              # maths function
from PIL                  import Image, ImageDraw # open images

# n*n - number of blocks
def FractalCount( a, n ):
    #print(a0[418, 440])
    count = 0
    size  = 500 // n
    n1, n2 = -size, 0
    
    for k in range(n*n): #проход по всем маленьким массивам большого массива
        if k % n== 0: 
            n1+=size
            n2=0
        else: 
            n2+=size
        #print(n1, n2)
        isblack = False
        for i in range(size): #гуляем по маленькому массиву
            
            if (isblack): break
            for j in range(size):
                #if (a[i+n1, j+n2]==255):
                    #print(a[i+n1][j+n2])
                
                if (a[i+n1, j+n2]==100):
                    #print(a[i+n1][j+n2])
                    count+=1
                    isblack = True
                    break
    return count
            
def Y(a0, n):
    #print(a0[418, 440])
    y0 = FractalCount(a0, n) 
    print(y0)
    if (y0>0): 
        return y0
        
    else: 
        return 1
    
#image = Image.open("карты/all_volga_.jpg") #Открываем изображение. 
#image = Image.open("hfhf.jpg") #Открываем изображение. 
image = Image.open("карты/рыбинское_1.jpg") #Открываем изображение. 
draw = ImageDraw.Draw(image) #Создаем инструмент для рисования. 
width = image.size[0] #Определяем ширину. 
height = image.size[1] #Определяем высоту. 	

pix = image.load() #Выгружаем значения пикселей.
a0 = np.asarray(image)
#print(a0)
factor = 10
for i in range(width):
    for j in range(height):
        ar = pix[i,j]
        if (ar > (((255 + factor) // 2))):
            a0[i,j]= 255#white
            draw.point(((i, j)), fill = 255)
        else:
            a0[i,j] = 100#black
            #print(i, j, a0[i, j])
            draw.point((i, j), fill= 100)
			
#image.save("ans.jpg", "JPEG")
fig, axs = plt.subplots(figsize=(9,9))
plt.imshow(image, cmap="gray")
axs.grid()
#plt.text(100, 100, 23, fontsize=10)

del draw

#print(a0[418, 440])
x = np.array([10, 20, 25, 50, 100])
y = np.array([Y(a0, 5), Y(a0, 20), Y(a0, 25), Y(a0, 50), Y(a0, 100)])
#x = np.array([5])
#y = np.array([Y(a0, 5)])
    #print(y)
x_log = (np.log(x)).reshape(-1, 1)
y_log = np.log(y)
model = LinearRegression().fit(x_log, y_log)
plt.text(0, 0, '%.2f' % model.coef_[0], fontsize=10,
             color = "green", rotation = 30)
    #print(model.coef_)
plt.show()
fig, axs = plt.subplots()
plt.loglog(x, y)