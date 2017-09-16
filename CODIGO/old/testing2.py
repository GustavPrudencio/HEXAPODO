import numpy as np
import MathModule as mm
from numpy import arctan2, sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D


def funcion(rotacion1,rotacion2,rotacion3, x):
    vector = np.array([[0],[x],[0]])
    vector1 = np.matmul(rotacion1,vector)
    vector2 = np.matmul(rotacion2,vector1)
    vector3 = np.matmul(rotacion3,vector2)
    return vector3
    
def rotaciongeneral(pi,pf,x):
        inicio = np.array([[pi[0]],[pi[1]],[pi[2]]])
        final = np.array([[pf[0]],[pf[1]],[pf[2]]])
        delta = final - inicio
        print(delta)
        angulos = arctan2([delta[2],delta[0],delta[1]],[delta[1],delta[2],delta[0]])
                
        Rz = mm.RotationMatrix([0,0,1])
        Rz[-angulos[2]]
        
        Rz[np.pi/2+angulos[2]]
        Ry = mm.RotationMatrix(np.matmul(Rz.matrix,[0,1,0]))
        Ry[angulos[1]]
        
##        Rx = mm.RotationMatrix([15,0,0])
##        Rx[angulos[0][0]]
        return funcion(np.eye(3),Ry.matrix,Rz.matrix,x)

Rx = mm.RotationMatrix([1,0,0])
Ry = mm.RotationMatrix([0,1,0])
Rz = mm.RotationMatrix([0,0,1])

grafrot1 = [funcion(np.eye(3),np.eye(3),Rx[np.pi/4],i) for i in range(-5,5)]
grafrot2 = [funcion(np.eye(3),np.eye(3),Ry[np.pi/4],i) for i in range(-5,5)]
grafrot3 = [funcion(np.eye(3),np.eye(3),Rz[-np.pi/4],i) for i in range(-5,5)]

grafrotado = [rotaciongeneral([0,0,0],[2,2,2],i) for i in range(-5,5)]
grafnorotado = [funcion(np.eye(3),np.eye(3),np.eye(3),i) for i in range(-5,5)]

fig = plt.figure()
ax = Axes3D(fig)
for k in grafrot1:
    ax.scatter(k[0],k[1],k[2],color='blue')
for k in grafrot2:
    ax.scatter(k[0],k[1],k[2],color='violet')
for k in grafrot3:
    ax.scatter(k[0],k[1],k[2],color='green')
for k in grafnorotado:
    ax.scatter(k[0],k[1],k[2],color='black')
for k in grafrotado:
    ax.scatter(k[0],k[1],k[2],color='turquoise')
ax.scatter(0,0,0,color="blue")
ax.scatter(1,1,1,color="red")
plt.show()
