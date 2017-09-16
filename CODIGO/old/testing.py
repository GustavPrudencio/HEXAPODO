import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from numpy import sqrt, absolute
import MathModule as mm

##matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
##vector = np.array([[1],[1],[1]])
##print(matrix)
##print(vector)
##
##multi = np.matmul(matrix,vector)
##
##print(multi)
##nodeberiafunciar = np.matmul(vector,matrix)
##print(nodeberiafunciar)
##efectivamente no funciona

Ry = mm.RotationMatrix([0,1,0])
Rx = mm.RotationMatrix([1,0,0])

fn1 = mm.ParabolicFunction(3)
fn2 = mm.ParabolicFunction(3)
fn3 = mm.ParabolicFunction(3)
fn4 = mm.ParabolicFunction(3)

fn2.rotate(Ry[np.pi/2])
fn3.rotate(Ry[np.pi/2])
fn4.rotate(Ry[np.pi/2])

fn3.translate([1,1,1])
fn4.translate([1,1,1])

fn4.rotate(Rx[np.pi/2])

print(str(fn1)+"\n"+"\n"+str(fn2)+"\n"+"\n"+str(fn3)+"\n"+"\n"+str(fn4)+"\n"+"\n")


##finalx = [fn1[k] for k in range(-10,10)]
##finaly = [fn2[k] for k in range(-10,10)]
##finalz = [fn3[k] for k in range(-10,10)]
##finalm = [fn4[k] for k in range(-10,10)]

finalx =[]
finaly =[]
finalz =[]
finalm =[]

for i in range(-10,11):
    if i <0:
        print(mm.longituddecurva(3,-sqrt(absolute(i)/3)))
        finalx.append(fn1[-sqrt(absolute(i)/3)])
        finaly.append(fn2[-sqrt(absolute(i)/3)])
        finalz.append(fn3[-sqrt(absolute(i)/3)])
        finalm.append(fn4[-sqrt(absolute(i)/3)])
    else:
        print(mm.longituddecurva(3,sqrt(i/3)))
        finalx.append(fn1[sqrt(i/3)])
        finaly.append(fn2[sqrt(i/3)])
        finalz.append(fn3[sqrt(i/3)])
        finalm.append(fn4[sqrt(i/3)])

fig = plt.figure()
ax = Axes3D(fig)

for k in finalx:
    ax.scatter(k[0],k[1],k[2],color='red')
for k in finalz:
    ax.scatter(k[0],k[1],k[2],color='violet')
for k in finaly:
    ax.scatter(k[0],k[1],k[2],color='blue')
for k in finalm:
    ax.scatter(k[0],k[1],k[2],color='black')
plt.show()


##al parecer todo funciona perfect!
