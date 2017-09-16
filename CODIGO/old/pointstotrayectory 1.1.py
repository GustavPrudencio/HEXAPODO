import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from MathModule import ParabolicFunction
from random import randint

def normalize(a):
    module = np.sqrt(np.dot(a,a))
    return np.dot(1/module,a)
    

class Trayectory:
    def __init__(self,pi,pf):
        self.pi=pi
        self.pf=pf
        pass
    def __getitem__(self,x):
        pi=self.pi  #punto incial
        pf=self.pf  #punto final
        inicio = np.array([pi[0],pi[1],pi[2]])
        final = np.array([pf[0],pf[1],pf[2]])
        delta = final - inicio #desplazamiento
        mdelta = np.sqrt(np.dot(delta,delta)) #módulo del desplazamiento
        normal = np.cross(delta,[0,0,1])
        normal = normalize(normal) # se normaliza la normal para solo tener la dirección y sentido
        para = ParabolicFunction(2/mdelta)   # se crea una parábola standard con concavidad
                                                # la mitad del módulo del delta
        # se obitene la proyeccion del vector en la dirección de la normal
        vector=np.array([para[x][0][0],para[x][1][0],para[x][2][0]]) 
        proy = np.dot(np.dot(normal,vector),normal)
        proy = np.array([[proy[0]],[proy[1]],[proy[2]]])

        #se hace una primera traslación de la parábola
        #tal que el vértice quede en la mitad del vector desplazamiento
        firsttranslate =np.dot(pf,0.5)+np.dot(pi,0.5)
        firsttranslate = np.array([[firsttranslate[0]],[firsttranslate[1]],[firsttranslate[2]]])#firsttranslate[2]
        para.translate(firsttranslate)

        print("delta: "+str(delta)+"\n\n punto inicial: "+str(pi)+"\n\npunto final: "+str(pf))

        #se desea realizar un segundo desplazamiento, tal que
        #los puntos inicial y final pertenezcan a la parábola
        delta = normalize(delta)
        wowy = pi[1]/(1-delta[0]**2)
        valor = np.array([[0],[0],[pi[0]-(-(mdelta/2)*wowy**2)]])
        print("\n\n wowy: "+str(wowy)+"\n\npunto inicial: "+str(pi)+"\n\npara: "+str(para[wowy])+"\n\n valor:"+str(valor)+"\n")
        para.translate(valor)


        return para[x]-proy
        
        
        

##a=[1,1,1]
##b=[0,0,1]
##a= normalize(a)
##b=normalize(b)
##
##normal = np.cross(a,b)


##normal = normalize(normal)
##print(normal)

inicio = np.array([1,1,1])
final = np.array([randint(-25,25),randint(-25,25),randint(-25,25)])
delta = final - inicio
mdelta = np.sqrt(np.dot(delta,delta))

a = ParabolicFunction(2/mdelta)
f =np.dot(final,0.5)+np.dot(inicio,0.5)
f = np.array([[f[0]],[f[1]],[f[2]]])
a.translate(f)

tray = Trayectory(inicio,final)
fig = plt.figure()
ax = Axes3D(fig)

graf = [tray[mdelta*k/10] for k in range(-10,10)]
graf33 = [a[k] for k in range(-10,10)]
for k in graf:
    ax.scatter(k[0],k[1],k[2],color='black')
for k in graf33:
    ax.scatter(k[0],k[1],k[2],color="violet")
ax.scatter(inicio[0],inicio[1],inicio[2],color="blue")
ax.scatter(final[0],final[1],final[2],color="red")
##ax2=[]
##ay=[]
##az=[]
##bx=[]
##by=[]
##bz=[]
##nx=[]
##ny=[]
##nz=[]
##for k in range(0,6):
##    ax2.append(k*a[0])
##    ay.append(k*a[1])
##    az.append(k*a[2])
##    
##    bx.append(k*b[0])
##    by.append(k*b[1])
##    bz.append(k*b[2])
##    
##    nx.append(k*normal[0])
##    ny.append(k*normal[1])
##    nz.append(k*normal[2])
##ax.plot(ax2,ay,az,color="blue")
##ax.plot(bx,by,bz,color="red")
##ax.plot(nx,ny,nz,color="violet")
##ax.scatter(0,0,0,color="black")
##ax.scatter(a[0],a[1],a[2],color="blue")
##ax.scatter(0,0,1,color="red")
##ax.scatter(normal[0],normal[1],normal[2],color="violet")
plt.show()
