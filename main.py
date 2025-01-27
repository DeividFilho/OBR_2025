####################################################################
# Criadores: Deivid e jean
# Versão: 1.0
# funções: curvas e andar reto com gyro, segue linha e verde.
# Pendencias: area de resgate, indentificação de rampa.             
####################################################################
from pybricks.hubs import PrimeHub
from pybricks.tools import wait, hub_menu

from Robotrush import run1


while(True):
    selected = hub_menu("1", "2", "3", "4")
    if selected == "1":
        print(1)
    elif selected == "2":
        run1()
        

   


    



