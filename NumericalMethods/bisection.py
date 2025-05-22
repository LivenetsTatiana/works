#вычисления
import math

e = 0.00001
n = 0
def BisectionMethod(a, b):
    n = 0
    x = (a + b) / 2
    while math.fabs(4*x - 8*math.sin(x) + 1) >= e:
        x = (a + b) / 2
        n+=1
        a, b = (a, x) if (4*a - 8*math.sin(a) + 1) * (4*x - 8*math.sin(x) + 1) < 0 else (x, b)
    print('Number of iteration n = ', n)
    return x

def Sin(x):
    n = 1
    sinx0 = (-1)**(n-1)*x**(2*n-1)/(2*n-1)
    sinx = sinx0
    while math.fabs(sinx0) >= e:
        n+=1
        sinx0*=(-1)*x**2/((2*n+1)*2*n)
        sinx+=sinx0
    return sinx

#построение графика
import pylab
import numpy
X = numpy.arange(-4, 4, 0.1)
pylab.plot([x for x in X], [(4*x - 8*math.sin(x) + 1) for x in X])
pylab.grid(True)

#вывод результата
print ('root 1 using bisection_method [0, 1]:%.6f' % BisectionMethod(0, 1))
print ('root 2 using bisection_method [1, 2]:%.6f' % BisectionMethod(1, 2))
