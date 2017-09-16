from numpy import array, matmul, eye, outer, cos, sin, asarray
from numpy import dot as product_dot
from numpy import cross as product_cross
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D
from numpy import sqrt, log
from math import sqrt

class ParabolicFunction:
    def __init__(self,concavidad):#concavidad -> Concavidad de la parabola. float/int
        self.concavidad = concavidad
        self.translation = array([0.,0.,0.]) #translation -> np.array
        self.translation_history = [array([0,0,0])]
        self.rotation = eye(3)

    def __str__(self):
        ## muestra la función evaluada en 1, su matriz de rotacion actual y su traslación
        original = (array([0,1,-self.concavidad*1**2]))
        string = ""
        string += "Funcion"+"\n"+str(original)+"\n"+"\n"
        string += "traslación: "+"\n"+str(self.translation)
        return string

    def translate(self,vector):#vector -> tralación de la parabola. type: Lista
        self.translation_history.append(array(vector))
        self.translation[0]=self.translation[0] + vector[0]
        self.translation[1]=self.translation[1] + vector[1]
        self.translation[2]=self.translation[2] + vector[2]

    def __getitem__(self,y):
        #y -> punto de evaluación. float/int
        original = (array([0,y,-self.concavidad*y**2]))
        original = matmul(self.rotation,original)
        original[0]=round(original[0] + self.translation[0],2)
        original[1]=round(original[1] + self.translation[1],2)
        original[2]=round(original[2] + self.translation[2],2)
        return original

    def __call__(self,x,y):
        original = (array([x,y,0]))
        original[0]=original[0] - self.translation[0]
        original[1]=original[1] - self.translation[1]
        original[2]=original[2] - self.translation[2]
        return original


    def rotate(self,rotmatrix):
        #rotmatrix -> Matriz para que se rote la curva. type: np.array
        self.rotation = matmul(self.rotation,rotmatrix)


def rotation_matrix(axis, theta):
    """
    Return the rotation matrix associated with counterclockwise rotation about
    the given axis by theta radians.
    """
    axis = asarray(axis)
    axis = axis/sqrt(product_dot(axis, axis))
    a = cos(theta/2.0)
    b, c, d = -axis*sin(theta/2.0)
    aa, bb, cc, dd = a*a, b*b, c*c, d*d
    bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
    return array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
                     [2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
                     [2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])
def ParabolicArcLength(concavity,x):
        return (1/2)*x*sqrt(4*concavity**2*x**2+1)+log(sqrt(4*concavity**2*x**2+1)+2*concavity*x)

if __name__ == "__main__":
    pass
