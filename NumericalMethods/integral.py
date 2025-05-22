import math
def f(x):
    return math.sqrt(1-1/2*(math.sin(x))**2)
def ftest(x):
    return x*x*x
def Trapezoid(a, b, n0, f, e):
    h = (b-a)/n0
    Im = h*(f(a)+f(b))/2
    I2m = Im/2
    x = a
    n=n0*2
    for i  in range(n0-1) :
        x+=h
        Im+=h*f(x)
        I2m+=h/2*(f(x-h/2)+f(x))
    h /=2
    while (math.fabs(I2m-Im)>=e):
        Im = I2m
        n*=2
        h/=2
        I2m = h*(f(a)+f(b))/2
        x=a
        m = 0
        for i in range(n-1) :
            x+=h
            I2m+=h*f(x)
    print('Метод трапеций: I2m = %.6f, 2m = %.0f, Ip по I2m и Im = %.6f' % (I2m, n, (4*I2m-Im)/3))

def Simpson(a, b, n0, f, e):
    h = (b-a)/n0
    Im = h*(f(a)+f(b))/3
    I2m = Im/2
    x = a
    n=n0*2
    for i in range(n0//2) :
        x+=2*h
        Im+=h*f(x)*2/3
        Im+=h*f(x-h)*4/3
    Im-=h*f(x)*2/3
    x = a
    h /= 2
    for i in range(n//2) :
        x+=2*h
        I2m+=h*f(x)*2/3
        I2m+=h*f(x-h)*4/3
    I2m-=h*f(x)*2/3
    while (math.fabs(I2m-Im)>=e):
        Im = I2m
        n*=2
        h/=2
        I2m = h*(f(a)+f(b))/3
        x=a
        for i in range(n//2) :
            x+=2*h
            I2m+=h*f(x)*2/3
            I2m+=h*f(x-h)*4/3
        I2m-=h*f(x)*2/3
    print('Метод Симпсона: I2m = %.6f, 2m = %.0f, Ip по I2m и Im = %.6f' % (I2m, n, (16*I2m-Im)/15))

Trapezoid(0, math.pi/2, 4, f, 0.00001)
Simpson(0, math.pi/2, 4, f, 0.00001)
