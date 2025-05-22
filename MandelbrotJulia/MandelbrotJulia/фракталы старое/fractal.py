print("dfhsf")# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
#x=5*np.ones(10)
import matplotlib.pyplot as plt
#plt.plot(x,x)
#fig, ax = plt.subplots()  # Create a figure containing a single axes.
#ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the axes.
#plt.plot([1, 2, 3, 4], [1, 4, 2, 3])
fig = plt.figure()  # an empty figure with no Axes
fig, axes = plt.subplots()  # a figure with a single Axes
#fig, axs = plt.subplots(2, 2)  # a figure with a 2x2 grid of Axes

x = np.linspace(0, 2, 100)

plt.plot(x, x, label='linear')  # Plot some data on the (implicit) axes.
plt.plot(x, x**2, label='quadratic')  # etc.
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()

# =============================================================================
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro') #построение по точкам 
# plt.axis([0, 6, 0, 20])
# plt.show()
# =============================================================================

# =============================================================================
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100
# 
# plt.scatter('a', 'b', c='c', s='d', data=data) #разный цвет и размер точек
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# plt.show()
# =============================================================================

# =============================================================================
# names = ['group_a', 'group_b', 'group_c']
# values = [1, 10, 100]
# 
# plt.figure(figsize=(9, 3))
# 
# plt.subplot(131) #колво строк, столбцов и номер графика
# plt.bar(names, values)
# plt.subplot(132)
# plt.scatter(names, values)
# plt.subplot(133)
# plt.plot(names, values)
# plt.suptitle('Categorical Plotting')
# plt.show()
# 
# =============================================================================

# =============================================================================
# def f(t):
#     return np.exp(-t) * np.cos(2*np.pi*t)
# 
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# 
# plt.figure()
# plt.subplot(211)
# plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# 
# plt.subplot(212)
# plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# plt.show()
# =============================================================================

# =============================================================================
# import matplotlib.pyplot as plt
# plt.figure(1)                # the first figure
# plt.subplot(211)             # the first subplot in the first figure
# plt.plot([1, 2, 3])
# plt.subplot(212)             # the second subplot in the first figure
# plt.plot([4, 5, 6])
# 
# 
# plt.figure(2)                # a second figure
# plt.plot([4, 5, 6])          # creates a subplot(111) by default
# 
# plt.figure(1)                # figure 1 current; subplot(212) still current
# plt.subplot(211)             # make subplot(211) in figure1 current
# plt.title('Easy as 1, 2, 3') # subplot 211 title
# =============================================================================

# =============================================================================
# ax = plt.subplot(111)
# 
# t = np.arange(0.0, 5.0, 0.01)
# s = np.cos(2*np.pi*t)
# line, = plt.plot(t, s, lw=2)
# 
# plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              )
# 
# plt.ylim(-2, 2)
# plt.show()
# =============================================================================

