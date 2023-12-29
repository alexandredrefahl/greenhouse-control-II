#!/usr/bin/python

import RPi.GPIO as GPIO           # import RPi.GPIO module  

# BCM = Numero da GPIO // BOARD = Numero do Pino
GPIO.setmode(GPIO.BOARD)          # choose BCM or BOARD
GPIO.setwarnings(False)		  # Desliga os avisos de pinos

pin_Fotop = 32
pin_Irrigacao = 35
pin_Fogger = 36
pin_Painel = 38
pin_Ventilador = 40

GPIO.setup(pin_Ventilador, GPIO.OUT) # set a port/pin as an output   
#GPIO.setup(pin_Painel, GPIO.OUT)  # set a port/pin as an input  
#GPIO.setup(pin_Fogger, GPIO.OUT)  # set a port/pin as an input  
#GPIO.setup(pin_Irrigacao, GPIO.OUT)  # set a port/pin as an input 
#GPIO.setup(pin_Fotop, GPIO.OUT) # set a port/pin as an output   

# O Raspberry utiliza logica invertida e por isso 0 = ON e 1 = OFF
GPIO.output(pin_Ventilador,0)
print("OK")
