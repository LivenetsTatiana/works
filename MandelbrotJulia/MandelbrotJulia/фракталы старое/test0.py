import random
def qusort(array, start, finish):
    mean = array[(start+finish)//2]
    left = start
    right = finish
    while left < right:
        while array[left] < mean:
            left += 1
        while array[right] > mean:
            right -= 1
        if left<=right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    if start<right:
        qusort(array, start, right)
    if left<finish:
        qusort(array, left, finish)

a=[]
for j in range(0, 10):
    a.append(random.randint(1, 15))
print(a)
qusort(a, 0, 9)
print(a)
