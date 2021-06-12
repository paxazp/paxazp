import math
import pylab
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy
from matplotlib.colors import LinearSegmentedColormap
from matplotlib import cm

def norma(x):
    maxim = -1
    for i in range(n+1):
        for j in range(n+1):
            if abs(x[i][j]) > maxim:
                maxim = abs(x[i][j])
    return maxim


#Шаг сетки    
h = 0.01
#Количество итераций
m = 4000

#Инициализация
n = math.floor(1/h)

u1 = [[10]*(n+1) for i in range(n+1)]
u2 = [[0]*(n+1) for i in range(n+1)]
r = [[0]*(n+1) for i in range(n+1)]

u3 = [[0]*(n+1) for i in range(n+1)]
u4 = [[0]*(n+1) for i in range(n+1)]

ut = [[0]*(n+1) for i in range(n+1)]

for i in range(n+1):
    u1[0][i] = 1
    u1[n][i] = 3
    u2[0][i] = 1
    u2[n][i] = 3
    u3[0][i] = 1
    u3[n][i] = 3
    u4[0][i] = 1
    u4[n][i] = 3
    u1[i][0] = 4
    u1[i][n] = 2
    u2[i][0] = 4
    u2[i][n] = 2
    u3[i][0] = 4
    u3[i][n] = 2
    u4[i][0] = 4
    u4[i][n] = 2



#Метод Якоби

for k in range(m):
    for i in range(1,n):
        for j in range(1,n):
            u2[i][j] = ((u1[i+1][j] + u1[i-1][j]) + (u1[i][j+1] + u1[i][j-1]))/4
            u4[i][j] = ((u3[i+1][j] + u3[i-1][j]) + (u3[i][j+1] + u3[i][j-1]))/4
        

    for i in range(n+1):
        for j in range(n+1):
            u1[i][j] = u2[i][j]
            u3[i][j] = u4[i][j]


#Матрица разности решений
            
for i in range(n+1):
        for j in range(n+1):
            ut[i][j] = u4[i][j] - u2[i][j]


#Вывод результата
print('Максимальная разность решений - ', norma(ut))

def makeData ():
    x = numpy.arange (0, 1+h, h)
    y = numpy.arange (0, 1+h, h)
    xgrid, ygrid = numpy.meshgrid(x, y)

    zgrid = numpy.matrix(u2)
    return xgrid, ygrid, zgrid


x, y, z = makeData()

fig = pylab.figure('Метод Якоби')

axes = Axes3D(fig)

axes.plot_surface(x, y, z, cmap = cm.viridis)

pylab.show()
