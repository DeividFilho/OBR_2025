####################################################################
# Criadores: Deivid e jean
# Versão: 1.0
# funções: curvas e andar reto com gyro, segue linha e verde.
# Pendencias: area de resgate, indentificação de rampa.             
####################################################################

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ColorSensor, Motor
from pybricks.parameters import Port,  Direction, Color,Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase

# definição de valores inicias(sensores, motores, canais and drive_base)
hub = PrimeHub()
left_motor = Motor(Port.E, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D)

Garra_E = Motor(Port.A)
Garra_D = Motor(Port.B)

drive_base = DriveBase(left_motor, right_motor, 56, 80)
velocidade = 100


def reset():
    # funçâo para reset de valores, de forma rapida
    hub.imu.reset_heading(0)
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)

def andareto(cms, pot):
    reset()
    while abs(right_motor.angle()) <= (cms*20.57)*1.6 and abs(left_motor.angle()) <= (cms*20.57)*1.6:
        drive_base.drive(pot, hub.imu.heading() * -9) # correção da direção com gyroscopio
        print(right_motor.angle())
    drive_base.stop()
    left_motor.hold()
    right_motor.hold()
    wait(140)

def curva(graus, pot): 
    reset()
    while abs(hub.imu.heading()) <= abs(graus):
        right_motor.run(((pot*-1)*graus)/abs(graus)) # calculo para definir a direção
        left_motor.run((pot*graus)/abs(graus)) 
        print(hub.imu.heading())
    left_motor.stop() 
    right_motor.stop()
    drive_base.stop()
    left_motor.hold()
    wait(140)

def motor_for_degrees(motores,velocidade, graus, esperar=True):
    motores.run_angle(velocidade, graus, wait=esperar)

def motor_até_degrees(motores1,velocidade1, graus1, esperar1=True):
    motores1.run_target(velocidade1, graus1,then=Stop.HOLD, wait=esperar1,)













    


