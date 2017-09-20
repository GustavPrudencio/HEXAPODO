import serial
from numpy import interp
#
import maestro
servos = maestro.Controller("COM8")
servos.setAccel(0,3)      #set servo 0 acceleration to 4
servos.setSpeed(0,80)
servos.setRange(0,4000,10000)
rotations = {0:True,6:True,12:True,3:False,9:False,16:False}
print(servos.getMax(0),servos.getMin(0))
angulo = 240
servos.setTarget(0,6000)
#[servos.setTarget(servo,1*(-1 if not rotations[servo] else 1)) for servo in rotations]
[servos.getPosition(servo) for servo in [0,3,6,9,12,16]]
servos.close
