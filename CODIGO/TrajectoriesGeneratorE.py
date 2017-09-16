import numpy as np
from numpy import array
from numpy import arange
from numpy import dot as product_dot
from numpy import cross as product_cross
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from MathFunctions import ParabolicFunction, rotation_matrix, ParabolicArcLength
from random import randint
from copy import copy
from math import fabs as abs
from math import sqrt

class Trayectory:
    def __init__(self,start_point,end_point,function='parabolic'):
        self.functions = {'parabolic':ParabolicFunction}
        # Se guardan las alturas de los puntos inicial y final:
        self.initial_z = start_point[2]
        self.final_z = end_point[2]

        self.start_point = [0,0,0]
        self.end_point = [0,0,0]
        self.start_point[0] = start_point[0]
        self.start_point[1] = start_point[1]
        self.start_point[2] = 0
        self.end_point[0] = end_point[0]
        self.end_point[1] = end_point[1]
        self.end_point[2] = 0

        # desplazamiento
        self.delta = [0,0,0]
        self.delta[0] = self.end_point[0]-self.start_point[0]
        self.delta[1] = self.end_point[1]-self.start_point[1]
        self.delta[2] = self.end_point[2]-self.start_point[2]
         #módulo del desplazamiento
        self.module = (self.delta[0]**2+self.delta[1]**2+self.delta[2]**2)**0.5

        # se crea una parábola standard con concavidad ocho divido en 3 veces el módulo del desplazamiento
        self.concavidad = 8/(3*self.module)
        self.function = self.functions[function](self.concavidad)
        # Se traslada la parábola standard tal que quedede a una altura adecuada para que el punto incial pertenezca
        self.function.translate([0,0,2*self.module/3])
        # Se normaliza el delta para proyectar la componente "y" en este.
        self.normalized_delta = [self.delta[0]/self.module,self.delta[1]/self.module,self.delta[2]/self.module]
        self.angle = 3.14*(-90+45)/180

#        normal = product_cross(array(self.delta),array([0,0,1]))
        # se normaliza la normal para solo tener la dirección y sentido
#        magnitude = (normal[0]**2+normal[1]**2+normal[2]**2)**0.5
#        self.normal = [0,0,0]
#        self.normal[0] = round(normal[0]/magnitude,2)
#        self.normal[1] = round(normal[1]/magnitude,2)
#        self.normal[2] = round(normal[2]/magnitude,2)

#        self.function.translate([0,self.norm/2,0])

#        self.fixed_height = [0,0,0]

        # Muestreamos para obtener el desfase
#        trayectoria_original = [self.function[k]
#                                for k in range(-int(self.norm),int(self.norm))
#                                if self.function[k][1]>=self.start_point[2] and self.function[k][1]<=int(self.norm)]
        # Se asume que existe un desfase solo en z
#        self.fixed_height[2] = abs(min(trayectoria_original[0][2],trayectoria_original[-1][2]))-self.start_point[2]


    def __getitem__(self, y):

        # Se crea el vector la función traslada en y en la mitad del módulo
        vector = [0,0,0]
        vector[0]=self.function[y][0]
        vector[1]=self.function[y][1]
        vector[2]=self.function[y-self.module/2][2]
        vector_final = [0,0,0]
        vector_final[0]=vector[1]*self.normalized_delta[0]
        vector_final[1]=vector[1]*self.normalized_delta[1]
        vector_final[2]=vector[2]
        vector_final = product_dot(rotation_matrix(self.normalized_delta,self.angle), vector_final)
        vector_translated = [0,0,0]
        vector_translated[0] = vector_final[0] + self.start_point[0]
        vector_translated[1] = vector_final[1] + self.start_point[1]
        vector_translated[2] = vector_final[2] + self.start_point[2] + self.initial_z
        return vector_translated

#    def __call__(self,percentage_interval_generator):
#        generator = (self[k]
#        for k in percentage_interval_generator
#        if self[k][2]>=0
#                )
#        return generator


def test():
    z = 0
#    inicio = [5*(2)**0.5,5*(2)**0.5,z]
#    final  = [5,5*(3)**0.5,z]
#    inicio = [14,7,z]
#    final  = [4,20,z]
    inicio = [randint(1,25),randint(1,25),z]
    final = [randint(1,25),randint(1,25),z]
    trayectoria = Trayectory(inicio,final)
#    intervalo = [k for k in arange(-100,100,1)]
#    puntos = [punto
#                            for punto in trayectoria(intervalo)
#                            ]
#    puntos = [trayectoria[k] for k in range(0,int(trayectoria.module)+1)]
    evaluacion = []
    for i in range(-6,0):
        evaluacion.append(i*trayectoria.concavidad*trayectoria.module**2/(4*6))
    evaluacion.append(-0.3*trayectoria.concavidad*trayectoria.module**2/(4*6))
    evaluacion.append(0*trayectoria.concavidad*trayectoria.module**2/(4*6))
    evaluacion.append(0.3*trayectoria.concavidad*trayectoria.module**2/(4*6))
    for i in range(1,7):
        evaluacion.append(i*trayectoria.concavidad*trayectoria.module**2/(4*6))

    puntos = []
    for k in evaluacion:
        if k < 0:
            puntos.append(trayectoria[-sqrt(abs(k)/trayectoria.concavidad)+trayectoria.module/2])
        elif k >= 0:
            puntos.append(trayectoria[sqrt(k/trayectoria.concavidad)+trayectoria.module/2])
    figura = plt.figure()
    axis = Axes3D(figura)


    for punto in puntos:
        axis.scatter(punto[0],punto[1],punto[2],color='black')
        #axis.scatter(punto[0],punto[1],punto[2]-trayectoria.fixed_height[2],color='black')
        # for punto in trayectoria_original:
        #     axis.scatter(trayectoria.normalized_delta[0]*punto[1],trayectoria.normalized_delta[1]*punto[1],trayectoria.normalized_delta[2]+(punto[2]+trayectoria.fixed_height[2]),color="violet")
    axis.scatter(inicio[0],inicio[1],inicio[2],color="blue")
    axis.scatter(final[0],final[1],final[2],color="red")
    axis.scatter(0,0,0,color="brown")
#        axis.scatter(0,trayectoria.norm,0,color="green")
    plt.show()
#    intervalo = [k for k in arange(-100,100,5)]
#    trayectoria_trasladada = [punto
#                            for punto in trayectoria(intervalo)
#                            ]
#    trayectoria_trasladada = sorted(trayectoria_trasladada, key = lambda punto : punto[2])


    # trayectoria_original = [trayectoria.function[k]
    #                         for k in range(-int(trayectoria.norm),int(trayectoria.norm))
    #                         if trayectoria.function[k][1]>=z and trayectoria.function[k][1]<=int(trayectoria.norm)]
    # trayectoria.fixed_height[2] = abs(min(trayectoria_original[0][2],trayectoria_original[-1][2]))-z
    # print(trayectoria.fixed_height)

    # Creamos el grafico

    # print(inicio,final)
#    traslacion = [trayectoria.delta[0]/2,trayectoria.delta[1]/2,trayectoria.delta[2]/2+trayectoria.norm/2]
if __name__ == "__main__":
    test()
