import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D

x = 2
class ParabolicFunction:
    def __init__(self,concavidad):#concavidad -> Concavidad de la parabola. float/int
        self.concavidad = concavidad
        self.rotation = RotationMatrix([0,1,0]) #rotation -> RotationMatrix
        self.translation = np.array([0,0,0]) #translation -> np.array
        
    def __str__(self):
        original = (np.array([1,-self.concavidad*1**2,0]))
        string = str(self.rotation*original)
        return string
        
    def translate(self,vector):#vector -> tralación de la parabola. Lista
        self.translation = np.array(vector)

    def rotate(self,rotmatrix): #rotmatrix -> Matriz para que se rote la curva. RotationMatrix
        self.rotation = self.rotation*rotmatrix

    def __getitem__(self,x): #x -> punto de evaluación. float/int
        original = (np.array([x,-self.concavidad*x**2,0]))
        if type(self.rotation) == type(RotationMatrix([0,1,0])): 
            rotation = self.rotation*original
        elif type(self.rotation) == type(np.array([])):
            rotation = np.matmul(self.rotation,original)
        return(self.translation+rotation)
###revisar __getitem__
class RotationMatrix:
    """ 3d rotation matrix"""
    def __init__(self,axis,angle = 0):  #axis   -> eje de rotación. Lista
                                        #angles -> angulo de rotación. float/int
        self.axis = np.array(axis)
        self.angle = angle
        self.matrix = None
        self[self.angle]

    def __str__(self):
        string = ""
        string += str(self.matrix)+"\n"
        string += "angulo : "+str(self.angle)+"\n"
        string += "axis : "+str(self.axis)+"\n"
        return string

    def __mul__(self,other):
        if isinstance(other,type(self)):#ambas son de la misma clase:
            return np.matmul(self.matrix,other.matrix)
        elif isinstance(other,type(np.array([]))):
            if len(other)==3:
                return np.matmul(self.matrix,other)
        return False

    def __getitem__(self,angle):
        # angulo en radianes
        # eje unitario
        #Angle es angulos de rotación
        self.angle = angle
        #d es el eje de rotación
        d = self.axis
        a = angle
        #identidad en R3:
        identidad = np.eye(3)
        #ddt es la multiplicación vectorial entre d y d transpuesto, el resultado es una matriz 3x3
        ddt = np.outer(d,d)
        skew = np.array( [[    0, d[2], -d[1]],
                          [-d[2],    0,  d[0]],
                          [ d[1],-d[0],     0]])
        #La matriz de rotacion es el resultado de la suma de ddt la skew multiplicada por
        #el seno del angulo y la identidad menos ddt multiplicada por el coseno del angulo
        matrix = ddt + np.cos(a)*(identidad - ddt) - np.sin(a)*skew
        #           [1,0,0]           ([1,0,0]  [1,0,0])        [0, 0,0]    [1,      0,     0]
        #matrix =   [0,0,0]  +  cos(q)([0,1,0] -[0,0,0]) -sen(q)[0, 0,1] =  [0,cos(q),-sen(q)]
        #           [0,0,0]           ([0,0,1]  [0,0,0])        [0,-1,0]    [0,sen(q), cos(q)]
        self.matrix = matrix
        return(self)


if __name__=='__main__':
    ##d = ParabolicFunction(1)
    ##print(d[2])
    ##d.translate([0,0,1])
    ##print(d[2])
    Rz = RotationMatrix([0,0,1])
    Rx = RotationMatrix([1,0,0])
    Ry = RotationMatrix([0,1,0])
    R1 = RotationMatrix([1,1,1])
    ## This bullshit is giving us trouble
    Rz = Rz[np.pi/2]
    Rx = Rx[np.pi/2]
    Ry = Ry[np.pi/2]
    R1 = R1[np.pi/2]
    print("matrices:\n")
    print(np.pi/2)
    print(Rx,Ry,Rz,R1)
    pz = ParabolicFunction(0.2)
    px = ParabolicFunction(0.2)
    py = ParabolicFunction(0.2)
    pm = ParabolicFunction(0.2)
    print("función evaluada en 2,\nsu matriz de rotación y el tipo de la matriz\n")
    print(pz)
    print(pz.rotation)
    print(str(type(pz.rotation)))
    original = [px[k] for k in range(-10,10)]
    px.rotate(Rx)
    pz.rotate(Rz)
    py.rotate(Ry)
    pm.rotate(Ry*Rz)
    print("lo mismo de antes, pero ahora la función está rotada")
    print(pz)
    print(pz.rotation)
    print(str(type(pz.rotation)))
    ###
    ###
    ### Hay que mejorar esa inconsistencia con los tipos,
    ### esto debería arreglar posibles problemas que tengamos
    ### en el futuro
    ###
    ###
    #p.translate([1,1,1])
    finalx = [px[k] for k in range(-10,10)]
    finalz = [pz[k] for k in range(-10,10)]
    finaly = [py[k] for k in range(-10,10)]
    finalm = [pm[k] for k in range(-10,10)]
    fig = plt.figure()
    ax = Axes3D(fig)
    for k in original:
        ax.scatter(k[0],k[1],k[2],color='black')
    for k in finalx:
        ax.scatter(k[0],k[1],k[2],color='blue')
    for k in finalz:
        ax.scatter(k[0],k[1],k[2],color='red')
    for k in finaly:
        ax.scatter(k[0],k[1],k[2],color='yellow')
    for k in finalm:
        ax.scatter(k[0],k[1],k[2],color='violet')
    plt.show()

    ##Ry = RotationMatrix([0,1,0])
    ##Rz = RotationMatrix([0,0,1])
    ##print(Ry)
    ##print(Rz)
    ##Ry[np.pi]
    ##Rz[np.pi]
    ##print(Ry)
    ##print(Rz)
    ##print(Ry*Rz)
    ##print(Rz*np.array([0,1,0]))
    ##print(Rz.matrix+np.array([[1,1,1],[1,1,1],[1,1,1]]))
