import numpy as np
from MathFunctions import *
from math import sqrt, atan2, cos, acos, sin, asin, pi


class Hexapodo:

    def __init__(self):
        self.origen = [0,0,0]
        self.extremidades = {}
        self.extremidades['10'] = None # Extremidad(self.origen + [1,0,0])
        self.extremidades['01'] = None # Extremidad(...)
        self.extremidades['20'] = None # Extremidad(...)
        self.extremidades['02'] = None # Extremidad(...)
        self.extremidades['30'] = None # Extremidad(...)
        self.extremidades['03'] = None # Extremidad(...)

    def avanzar_norte(self):
        pass

    def avanzar_sur(self):
        pass

    def avanzar_este(self):
        pass

    def avanzar_oeste(self):
        pass

class Extremidad:

    def __init__(self, leg = [2.5,7.4,11.4]):
        self.posicion_actual=None
        self.origen=None
        self.leg = leg

    def InverseKinematics(self,vector):
        # Le entra un vector <vector> posición de la punta de la extremidad.
        # Retorna un vector <angulos> con los ángulos que debería tomar el servo.
        # El angulo[0] sería el del servo más próximo al cuerpo del hexápodo.
        #    angulo[1] sería el siguiente y angulo[2] el último.
        # Los ángulos están en radianes.
        # c, B, h, C1 y C2 son creadas para realizar los cálculos
        [x,y,z] = vector
        angulos = [0,0,0]

        angulos[0]=atan2(y,x)
        c=((x-self.leg[0]*cos(angulos[0]))**2+(y-self.leg[0]*sin(angulos[0]))**2+z**2)**0.5
        B=acos((-self.leg[2]**2+self.leg[1]**2+c**2)/(2*self.leg[1]*c))
        angulos[1]=asin(-z/c)-B
        C1=pi/2-B
        h=self.leg[1]*sin(B)
        C2=acos(h/self.leg[2])
        angulos[2]=pi-C1-C2
        return angulos

    def generar_trayectoria(self,posicion_actual,posicion_final):
        # matrices y wea
        # return [punto1,punto2,punto3.......]
        pass

    def avanzar(self,posicion_final):
        # desarrollar...
        posiciones = self.generar_trayectoria(self.posicion_actual,posicion_final)
        try:
            estados = [Estado(posicion,cinematica_inversa(posicion)) for posicion in posiciones]
        except:
            'Posiciones no validas'
        self.posicion_actual=estados[-1]
        return(estados)


class Estado:

    def __init__(self,cart=[0,0,0],ang=[0,0,0]):
        self.cart = np.array(cart)
        self.ang = np.array(ang)

    def rotar(self,matrix):
        pass

    def __add__(self,other):
        pass

if __name__=='__main__':
    pass
