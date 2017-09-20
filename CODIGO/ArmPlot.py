import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import matplotlib as mpl
from TrajectoriesGeneratorE import *
from math import cos, sin, pi
from Control import *
from random import randint


class Simulation:
    def __init__(self):
        # Se define el largo constante de las extremidades:
        self.leg= [2.5,7.4,11.4]
        # Los objetos necesarios para graficar:
        self.fig= plt.figure()
        self.ax = self.fig.add_subplot(111, projection="3d")

#    def InverseKinematics(self,vector):
#        # Le entra un vector <vector> posición de la punta de la extremidad.
#        # Retorna un vector <angulos> con los ángulos que debería tomar el servo.
#        # c, B, h, C1 y C2 son creadas para realizar los cálculos
#        [x,y,z] = vector
#        angulos = [0,0,0]
#
#        angulos[0]=atan2(y,x)
#        c=((x-self.leg[0]*cos(angulos[0]))**2+(y-self.leg[0]*sin(angulos[0]))**2+z**2)**0.5
#        B=acos((-self.leg[2]**2+self.leg[1]**2+c**2)/(2*self.leg[1]*c))
#        angulos[1]=asin(-z/c)-B
#        C1=pi/2-B
#        h=self.leg[1]*sin(B)
#        C2=acos(h/self.leg[2])
#        angulos[2]=pi-C1-C2
#        return angulos

    def ArmPlot(self,vector):
        # Entra un vector posición de la punta de la extremidad.
        # Grafica una simulación de las distintas posiciones que debería tomar la pata.
        pata = Extremidad()
        angulos = pata.InverseKinematics(vector)
        # La pata de un insecto está formada por coxa, femur, tibia (y tarsus)
        origin  = [0,0,0]
        coxa    = [0,0,0]
        femur   = [0,0,0]
        tibia   = [0,0,0]

        #Se calculan los puntos que deberían tomar la punta de cada parte de la pata
        coxa[0] = self.leg[0]*cos(angulos[0])
        coxa[1] = self.leg[0]*sin(angulos[0])
        coxa[2] = 0
        femur[0] = (self.leg[0]+self.leg[1]*cos(angulos[1]))*cos(angulos[0])
        femur[1] = (self.leg[0]+self.leg[1]*cos(angulos[1]))*sin(angulos[0])
        femur[2] = -self.leg[1]*sin(angulos[1])
        tibia[0] = (self.leg[0]+self.leg[2]*cos(angulos[2]+angulos[1])+self.leg[1]*cos(angulos[1]))*cos(angulos[0])
        tibia[1] = (self.leg[0]+self.leg[2]*cos(angulos[2]+angulos[1])+self.leg[1]*cos(angulos[1]))*sin(angulos[0])
        tibia[2] = -self.leg[1]*sin(angulos[1])-self.leg[2]*sin(angulos[2]+angulos[1])

        # Para graficar los puntos:
        Points_x=[origin[0],coxa[0],femur[0],tibia[0]]
        Points_y=[origin[1],coxa[1],femur[1],tibia[1]]
        Points_z=[origin[2],coxa[2],femur[2],tibia[2]]

        # Finalmente se gráfica:
        self.ax.scatter(Points_x, Points_y, Points_z,s=[10,1,1,1])
        self.ax.plot([origin[0],coxa[0]],[origin[1],coxa[1]],[origin[2],coxa[2]],linewidth=0.3)
        self.ax.plot([ coxa[0],femur[0]],[ coxa[1],femur[1]],[ coxa[2],femur[2]],linewidth=0.3)
        self.ax.plot([femur[0],tibia[0]],[femur[1],tibia[1]],[femur[2],tibia[2]],linewidth=0.3)
#
#def  ArmPlot(X):
#    #Parametros:
#    x=X[0]
#    y=X[1]
#    z=X[2]
#    X_o=[0,0,0]
#    l0=2.5
#    l1=7.4
#    l2=11.4
#
#    #cinematica inversa
#    t1=math.atan2(y,x)
#    c=((x-l0*math.cos(t1))**2+(y-l0*math.sin(t1))**2+z**2)**0.5
#    B=math.acos((-l2**2+l1**2+c**2)/(2*l1*c))
#    t2=math.asin(-z/c)-B
#    C1=math.pi/2-B
#    h=l1*math.sin(B)
#    C2=math.acos(h/l2)
#    t3=math.pi-C1-C2
#    T=[[1,t1],[2,t2],[3,t3]]
#
#    #PLoteo
#    x1=X_o[0]
#    y1=X_o[1]
#    z1=X_o[2]
#    x2=l0*math.cos(t1)
#    y2=l0*math.sin(t1)
#    z2=0
#    x3=(l0+l1*math.cos(t2))*math.cos(t1)
#    y3=(l0+l1*math.cos(t2))*math.sin(t1)
#    z3=-l1*math.sin(t2)
#    x4=(l0+l2*math.cos(t3+t2)+l1*math.cos(t2))*math.cos(t1)
#    y4=(l0+l2*math.cos(t3+t2)+l1*math.cos(t2))*math.sin(t1)
#    z4=-l1*math.sin(t2)-l2*math.sin(t3+t2)
#    x_a=[x1,x2,x3,x4]
#    y_a=[y1,y2,y3,y4]
#    z_a=[z1,z2,z3,z4]
#
#
#    o = [1 for n in range(len(x_a))]
#    o[0]=o[0]+9
#    print(o)
#    ax.scatter(x_a, y_a, z_a,s=o)
#    ax.plot([x1,x2],[y1,y2],[z1,z2],linewidth=0.3)
#    ax.plot([x2,x3],[y2,y3],[z2,z3],linewidth=0.3)
#    ax.plot([x3,x4],[y3,y4],[z3,z4],linewidth=0.3)
#
#def trajectory_calc(a, b,mod_zyx=(0, 0, 0), right=True, samples=30, debug=True):
#    t = np.linspace(0, a, samples)
#    x = [t_ + mod_zyx[0] for t_ in t]
#    z = [(1 if right else -1) * (b - ((4*b)/(a**2))*((t_-a/2)**2)) + mod_zyx[1] for t_ in t]
#    y = [(1 if right else 1) * (b - ((4*b)/(a**2)) * ((t_-a/2)**2) + mod_zyx[2]) for t_ in t]
#    if debug:
#        mpl.rcParams['legend.fontsize'] = 10
#        fig_ = plt.figure()
#        ax_ = fig_.gca(projection='3d')
#        ax_.plot(*(x, y, z), label='curve')
#        ax_.legend()
#        plt.show(block=True)
#    return ([x, y, z])

if __name__=="__main__":
    pata = Extremidad()
    #z = -randint(3,10)
    #inicio = [float(randint(4,10)),-float(randint(3,10)),float(z)]
    z = -7
    inicio = [5,0,z]
    angulo = (-180+20)*pi/180
    distancia = 10
    final = [0,0,0]
    final[0]  = inicio[0]+[distancia*cos(angulo),distancia*sin(angulo),float(z)][0]
    final[1]  = inicio[1]+[distancia*cos(angulo),distancia*sin(angulo),float(z)][1]
    final[2]  = inicio[2]
    print([cos(angulo),sin(angulo),0])
    print(inicio)
    print(final)
    trayectoria = Trayectory(inicio,final)
    print(trayectoria.module)
    print(trayectoria.normalized_delta)
    evaluacion = []
    for i in range(-6,0):
        evaluacion.append(i*trayectoria.concavidad*trayectoria.module**2/(4*6))
    evaluacion.append(-0.3*trayectoria.concavidad*trayectoria.module**2/(4*6))
    evaluacion.append(0*trayectoria.concavidad*trayectoria.module**2/(4*6))
    evaluacion.append(0.3*trayectoria.concavidad*trayectoria.module**2/(4*6))
    for i in range(1,7):
        evaluacion.append(i*trayectoria.concavidad*trayectoria.module**2/(4*6))

    trayectoria_trasladada = []
    for k in evaluacion:
        if k < 0:
            trayectoria_trasladada.append(trayectoria[-sqrt(abs(k)/trayectoria.concavidad)+trayectoria.module/2])
        elif k >= 0:
            trayectoria_trasladada.append(trayectoria[sqrt(k/trayectoria.concavidad)+trayectoria.module/2])
#    z = 0
#    inicio = [8,-10,z]
#    final  = [8,10,z]
#    intervalo = [k for k in arange(-100,100,5)]
#    trayectoria = Trayectory(inicio,final)
#    trayectoria_trasladada = [punto
#                            for punto in trayectoria(intervalo)
#                            ]
    #trayectoria_trasladada = sorted(trayectoria_trasladada, key = lambda punto : punto[2])

    error = 0

    sim = Simulation()
    for k in range(0,len(trayectoria_trasladada)):
        try:
            vector = [0,0,0]
            vector[0] = trayectoria_trasladada[k][0]
            vector[1] = trayectoria_trasladada[k][1]
            vector[2] = trayectoria_trasladada[k][2]
            sim.ArmPlot(vector)
            print("Para el vector N°"+str(k)+" se obtienen los ángulos: ", pata.InverseKinematics(vector))
        except:
            error+=1
            vector = [0,0,0]
            vector[0] = trayectoria_trasladada[k][0]
            vector[1] = trayectoria_trasladada[k][1]
            vector[2] = trayectoria_trasladada[k][2]
            print("no pude plotear: ",vector)
        try:
            sim.ax.plot([trayectoria_trasladada[k][0],trayectoria_trasladada[k+1][0]],[trayectoria_trasladada[k][1],trayectoria_trasladada[k+1][1]],[trayectoria_trasladada[k][2],trayectoria_trasladada[k+1][2]])
        except:
            None

#    fig = plt.figure()
#    ax = fig.add_subplot(111, projection='3d')
#
#    for k in range(0,len(trayectoria_trasladada)):
#        try:
#            ArmPlot(trayectoria_trasladada[k])
#            print(trayectoria_trasladada[k])
#        except:
#            error+=1
#            print("no pude plotear: ",trayectoria_trasladada[k])
#        try:
#            ax.plot([trayectoria_trasladada[k][0][0],trayectoria_trasladada[k+1][0][0]],[trayectoria_trasladada[k][1][0],trayectoria_trasladada[k+1][1][0]],[trayectoria_trasladada[k][2][0],trayectoria_trasladada[k+1][2][0]])
#        except:
#            None
#####    temp=trajectory_calc(10,15,(-5,-15,0),debug=False)
#####    x=temp[0]
#####    y=temp[1]
#####    z=temp[2]
#####    error=0
#####
#####    for i in range(len(x)):
#####        a=[x[i],y[i],z[i]]
#####        try:
#####            Plot(a)
#####        except:
#####            error+=1
#####        try:
#####            ax.plot([x[i],x[i+1]],[y[i],y[i+1]],[z[i],z[i+1]])
#####        except:
#####            None
    print(error)
    sim.ax.scatter(inicio[0],inicio[1],inicio[2],color="red")
    sim.ax.scatter(final[0],final[1],final[2],color="blue")
    sim.ax.set_xlabel('X Label')
    sim.ax.set_ylabel('Y Label')
    sim.ax.set_zlabel('Z Label')
    ## el cero para el angulo[0] sería a lo largo del eje y
    plt.show()
