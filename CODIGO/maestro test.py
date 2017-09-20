import serial
from numpy import interp
#
import maestro
servos = maestro.Controller("COM8")
##Posiciones del hexápodo desde fuera a dentro.
##izquierda     derecha
##0-1-2   	    3-4-5
##6-7-8        	9-10-11
##12-13-14 	    16-15-17
servos.setAccel(0,3)      #set servo 0 acceleration to 4
servos.setSpeed(0,80)
servos.setRange(0,3000,9500)#3000 más arriba, 9500 más abajo
servos.setTarget(0,3000)
servos.setAccel(1,3)      #set servo 0 acceleration to 4
servos.setSpeed(1,80)
servos.setRange(1,3000,10000)#10000 más arriba, 3000 más abajo
servos.setTarget(1,10000)
servos.setAccel(2,3)      #set servo 0 acceleration to 4
servos.setSpeed(2,80)
servos.setRange(2,3000,10000)#10000 más dercha, 3000 más izquierda visto desde atrás
servos.setTarget(2,6000)
#rotations = {0:True,6:True,12:True,3:False,9:False,16:False}
#print(servos.getMax(0),servos.getMin(0))
#angulo = 240
#servos.setTarget(0,6000)
#[servos.setTarget(servo,1*(-1 if not rotations[servo] else 1)) for servo in rotations]
#[servos.getPosition(servo) for servo in [0,3,6,9,12,16]]
servos.close
