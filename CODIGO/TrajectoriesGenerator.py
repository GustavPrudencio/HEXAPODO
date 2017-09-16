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

class Trayectory:
    def __init__(self,start_point,end_point,function='parabolic'):
        self.functions = {'parabolic':ParabolicFunction}
        # por ahora solo soporta puntos en z = 0
        self.start_point = start_point
        self.end_point = end_point
        # desplazamiento
        self.delta = [0,0,0]
        self.delta[0] = self.end_point[0]-self.start_point[0]
        self.delta[1] = self.end_point[1]-self.start_point[1]
        self.delta[2] = self.end_point[2]-self.start_point[2]
         #módulo del desplazamiento
        self.norm = (self.delta[0]**2+self.delta[1]**2+self.delta[2]**2)**0.5

        self.normalized_delta = [self.delta[0]/self.norm,self.delta[1]/self.norm,self.delta[2]/self.norm]
        normal = product_cross(array(self.delta),array([0,0,1]))
        # se normaliza la normal para solo tener la dirección y sentido
        magnitude = (normal[0]**2+normal[1]**2+normal[2]**2)**0.5
        self.normal = [0,0,0]
        self.normal[0] = round(normal[0]/magnitude,2)
        self.normal[1] = round(normal[1]/magnitude,2)
        self.normal[2] = round(normal[2]/magnitude,2)
        # se crea una parábola standard con concavidad la mitad del módulo del delta
        self.function = self.functions[function](2/self.norm)

        self.function.translate([0,self.norm/2,0])

        self.fixed_height = [0,0,0]

        # Muestreamos para obtener el desfase
        trayectoria_original = [self.function[k]
                                for k in range(-int(self.norm),int(self.norm))
                                if self.function[k][1]>=self.start_point[2] and self.function[k][1]<=int(self.norm)]
        # Se asume que existe un desfase solo en z
        self.fixed_height[2] = abs(min(trayectoria_original[0][2],trayectoria_original[-1][2]))-self.start_point[2]

        self.angle = 3.14*15/180

    def __getitem__(self, percentage):

        x = self.norm*percentage/100

        vector = [0,0,0]
        vector[0]=self.function[x][0]+self.fixed_height[0]
        vector[1]=self.function[x][1]+self.fixed_height[1]
        vector[2]=self.function[x][2]+self.fixed_height[2]
        vector_final = [0,0,0]
        vector_final[0]=vector[1]*self.normalized_delta[0]
        vector_final[1]=vector[1]*self.normalized_delta[1]
        vector_final[2]=self.normalized_delta[2]+vector[2]
        vector_rotated = product_dot(rotation_matrix(self.normalized_delta,self.angle), vector_final)
        vector_translated = vector_rotated + self.start_point
        return vector_translated

    def __call__(self,percentage_interval_generator):
        generator = (self[k]
                    for k in percentage_interval_generator
                    if self.function[self.norm*k/100][1]>=0 and self.function[self.norm*k/100][1]<=int(self.norm)
                    )
        return generator


def test():
    z = 0
    inicio = [randint(1,25),randint(1,25),z]
    final  = [randint(1,25),randint(1,25),z]
    intervalo = [k for k in arange(-100,100,5)]
    trayectoria = Trayectory(inicio,final)
    trayectoria_trasladada = [punto
                            for punto in trayectoria(intervalo)
                            ]
    trayectoria_trasladada = sorted(trayectoria_trasladada, key = lambda punto : punto[2])


    # trayectoria_original = [trayectoria.function[k]
    #                         for k in range(-int(trayectoria.norm),int(trayectoria.norm))
    #                         if trayectoria.function[k][1]>=z and trayectoria.function[k][1]<=int(trayectoria.norm)]
    # trayectoria.fixed_height[2] = abs(min(trayectoria_original[0][2],trayectoria_original[-1][2]))-z
    # print(trayectoria.fixed_height)

    # Creamos el grafico
    figura = plt.figure()
    axis = Axes3D(figura)

    # print(inicio,final)
    traslacion = [trayectoria.delta[0]/2,trayectoria.delta[1]/2,trayectoria.delta[2]/2+trayectoria.norm/2]
    for punto in trayectoria_trasladada:
        axis.scatter(punto[0],punto[1],punto[2],color='black')
        #axis.scatter(punto[0],punto[1],punto[2]-trayectoria.fixed_height[2],color='black')
    # for punto in trayectoria_original:
    #     axis.scatter(trayectoria.normalized_delta[0]*punto[1],trayectoria.normalized_delta[1]*punto[1],trayectoria.normalized_delta[2]+(punto[2]+trayectoria.fixed_height[2]),color="violet")
    axis.scatter(inicio[0],inicio[1],inicio[2],color="blue")
    axis.scatter(final[0],final[1],final[2],color="red")
    axis.scatter(0,trayectoria.norm,0,color="green")
    plt.show()
if __name__ == "__main__":
    while True:
        test()
