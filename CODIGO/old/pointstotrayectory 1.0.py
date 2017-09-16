import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from numpy import sqrt, absolute, arctan2
import MathModule as mm

##Let's say we have 2 points pi = (pi1,pi2,pi3) and pf = (pf1,pf2,pf3)
##we can get the displacement vector delta = pf-pi
##now, we want a bunch of things:
##first, these points have to belong to the parabolic function
##second, we want to rotate this function in order for it to be suitable for movement
##third, we also want a suitable concavity
##how are we gonna do it? find out with me:

class Trayectory:
    def __init__(self):
        pass
    def PointstoParabolic(self,pi,pf):
        inicio = np.array([[pi[0]],[pi[1]],[pi[2]]])
        final = np.array([[pf[0]],[pf[1]],[pf[2]]])
        delta = final - inicio
        para = mm.ParabolicFunction(3)
        angulos = arctan2([delta[2],delta[0],delta[1]],[delta[1],delta[2],delta[0]])
        
        Rz = mm.RotationMatrix([0,0,1])
        Rz[angulos[2]]
        para.rotate(Rz.matrix)
        
        Rz[np.pi/2-angulos[2]]
        Ry = mm.RotationMatrix(np.matmul(Rz.matrix,[0,1,0]))
        Ry[angulos[1]]
        para.rotate(Ry.matrix)
        
##        Rx = mm.RotationMatrix([1,0,0])
##        Rx[angulos[0]]
##        para.rotate(Rx.matrix)
        firsttranslate =np.dot(pf,0.5)+np.dot(pi,0.5)
        firsttranslate = np.array([[firsttranslate[0]],[firsttranslate[1]],[firsttranslate[2]]])
        para.translate(firsttranslate)
##        deltamodule = np.dot(delta.T,delta)
##        oldfinalpoint = para[deltamodule[0][0]/2]
##        para.translate(final - oldfinalpoint)
        return para
        
        
        
        ##angulos de la delta con respecto al eje coordenado    
a = Trayectory()
parabola = a.PointstoParabolic([1,1,1],[3,2,3])
print(parabola)

graf = [parabola[k] for k in range(-4,4)]
fig = plt.figure()
ax = Axes3D(fig)
for k in graf:
    ax.scatter(k[0],k[1],k[2],color='black')
ax.scatter(1,1,1,color="blue")
ax.scatter(3,2,3,color="red")
plt.show()


##print(np.array([[4],[3],[2]])-np.array([[1],[1],[1]]))
##angul = arctan2([2,3,4],[3,2,1])
##print(str(angul[0])+str(type(angul[0])))
