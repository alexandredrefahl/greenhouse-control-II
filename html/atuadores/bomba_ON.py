#!/usr/bin/python

import RPi.GPIO as GPIO           # import RPi.GPIO module

# BCM = Numero da GPIO // BOARD = Numero do Pino
GPIO.setmode(GPIO.BOARD)          # choose BCM or BOARD
GPIO.setwarnings(False)       # Desliga os avisos

pin_Fotop = 26
pin_Irrigacao = 35
pin_Fogger = 36
pin_Painel = 38
pin_Ventilador = 40

pin_Bomba = 29


#GPIO.setup(pin_Ventilador, GPIO.OUT) # set a port/pin as an output
#GPIO.setup(pin_Painel, GPIO.OUT)  # set a port/pin as an input
#GPIO.setup(pin_Fogger, GPIO.OUT)  # set a port/pin as an input
#GPIO.setup(pin_Irrigacao, GPIO.OUT)  # set a port/pin as an input
GPIO.setup(pin_Bomba, GPIO.OUT)  # set a port/pin as an input

# No caso do pino direto da bomba 0 = OFF e 1 = ON
GPIO.output(pin_Bomba,1)
print("OK")
