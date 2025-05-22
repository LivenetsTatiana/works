import math

e = 0.00001
n = 0
def SimpleIterationMethod(a, b, t):
    n = 0
    x = (a + b) / 2
    while math.fabs(4*x - 8*math.sin(x) + 1) >= e:
        x = x + t*(4*x - 8*math.sin(x) + 1)
        n+=1
    print('Number of iteration n = ', n)
    return x

#вывод результата
print ('root 1 using iteration_method [0, 1] topt=2/7: %.6f' % (SimpleIterationMethod(0, 0.5, 2/7)))
print ('root 2 using iteration_method [1, 2] topt=-1/8: %.6f' % (SimpleIterationMethod(1.5, 2, -0.125)))
