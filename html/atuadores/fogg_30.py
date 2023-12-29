#!/usr/bin/python

import RPi.GPIO as GPIO           # import RPi.GPIO module
import time

# BCM = Numero da GPIO // BOARD = Numero do Pino
GPIO.setmode(GPIO.BOARD)          # choose BCM or BOARD
GPIO.setwarnings(False)		  # Desliga os avisos de pinos

pin_Fotop = 32
pin_Irrigacao = 35
pin_Fogger = 36
pin_Painel = 38
pin_Ventilador = 40

# Tempo em segundos
tempo=20

GPIO.setup(pin_Fogger, GPIO.OUT)  # set a port/pin as an input

# O Raspberry utiliza logica invertida e por isso 0 = ON e 1 = OFF
GPIO.output(pin_Fogger,0)
print("Ligado por " + str(tempo) + " segundos")

# Aguarda o tempo determinado
time.sleep(tempo)

# Desliga o fogger
GPIO.output(pin_Fogger,1)
