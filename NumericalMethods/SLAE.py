import numpy as np
from numpy import linalg as la
a = np.array([[1, -0.22, 0.11, -0.31, 2.7], [-0.38, 1, 0.12, -0.22, -1.5],
[-0.11, -0.23, 1, 0.51, 1.2], [-0.17, 0.21, -0.31, 1, -0.17]], float)
e=0.01
print('Исходная матрица\n', a)
np.set_printoptions(precision=7)
#--------Гаусс
def GaussTo(array):
    for nrow, row in enumerate(array):
        div = row[nrow]
        row /= div #делим строку на диагональный элемент
        for row_down in array[nrow+1:]: #вычитаем эту приведенную строку из остальных
            factor = row_down[nrow]
            row_down -= factor*row
    return array
def GaussFrom(array):
    for nrow in range(len(array)-1,0,-1):
        row = array[nrow]
        for row_up in array[:nrow]:
            factor = row_up[nrow]
            row_up -= factor*row
    return array
a1=a.copy()
GaussTo(a1)
GaussFrom(a1)
print('-----Метод Гаусса(точный)-----')
print(a1[:,4])
#--------домножение на транспонированную матрицу
at=np.transpose(a[:,[0, 1, 2, 3]])
b=at@a[:,[0, 1, 2, 3]]
f=at@a[:,4]
#--------Метод наискорейшего спуска
def SteepestDescent(A, f, x0, e):
    rn=A@x0-f
    n=0
    xn=x0
    while (la.norm(rn, ord=2)>=e):
        tn=np.dot(rn, rn)/np.dot(A@rn, rn)
        x0=xn
        xn=xn-tn*rn
        n+=1
        rn=A@xn-f
    print("Погрешность в методе наискорейшего спуска = ", e)
    print("Количество итераций для этой погрешности = ", n)
    return xn
b1=b.copy()
f1=f.copy()
x0 = np.transpose(np.array([0, 0, 0, 0], float))
print('-----Метод Наискорейшего спуска(приближенный)-----')
print('x0 = ', x0)
for i in range(6):
    print('x = ', SteepestDescent(b1, f1, x0, e))
    e/=10
#--------Метод сопряженных градиентов
def ConjugateGradient(A, f, x0, e):
    rn=A@x0-f
    pn=rn
    n=0
    xn=x0
    while (la.norm(rn, ord=2)>=e):
        tn=np.dot(rn, pn)/np.dot(A@pn, pn)
        xn=xn-tn*pn
        rn=A@xn-f
        bn=np.dot(rn, A@pn)/np.dot(A@pn, pn)
        pn = rn -bn*pn
        n+=1
    print("Погрешность в методе сопряженных градиентов = ", e)
    print("Количество итераций для этой погрешности = ", n)
    return xn

print('-----Метод сопряженных градиентов(приближенный)-----')
print('x0 = ', x0)
e=0.01
for i in range(6):
    print('x = ', ConjugateGradient(b1, f1, x0, e))
    e/=10
