#!/usr/bin/python

import RPi.GPIO as GPIO                 # import RPi.GPIO module

# BCM = Numero da GPIO // BOARD = Numero do Pino
GPIO.setmode(GPIO.BOARD)                # choose BCM or BOARD
GPIO.setwarnings(False)                 # Desliga os avisos

# Estufa 2
pin_Fotoperiodo = 26
pin_Irrigacao = 35
pin_Fogger = 36
pin_Painel = 38
pin_Ventilador = 40

# Estufa 1
pin_Linha1 = 33
pin_Linha2 = 32
pin_Linha3 = 37
pin_Linha4 = 31
pin_Bomba = 29

GPIO.setup(pin_Ventilador, GPIO.OUT)    # set a port/pin as an output
GPIO.setup(pin_Painel, GPIO.OUT)        # set a port/pin as an input
GPIO.setup(pin_Fogger, GPIO.OUT)        # set a port/pin as an input
GPIO.setup(pin_Irrigacao, GPIO.OUT)     # set a port/pin as an input
GPIO.setup(pin_Fotoperiodo, GPIO.OUT)   # set a port/pin as an input

GPIO.setup(pin_Linha1, GPIO.OUT)
GPIO.setup(pin_Linha2, GPIO.OUT)
GPIO.setup(pin_Linha3, GPIO.OUT)
GPIO.setup(pin_Linha4, GPIO.OUT)
GPIO.setup(pin_Bomba,  GPIO.OUT)

# Raspberry trabalha com logica invertida por isso 0 = ON e 1 = OFF
GPIO.output(pin_Fotoperiodo,1)
GPIO.output(pin_Irrigacao,1)
GPIO.output(pin_Fogger,1)
GPIO.output(pin_Painel,1)
GPIO.output(pin_Ventilador,1)

# Todos estes trabalham com logica invertida
GPIO.output(pin_Linha1, 1)
GPIO.output(pin_Linha2, 1)
GPIO.output(pin_Linha3, 1)
GPIO.output(pin_Linha4, 1)
GPIO.output(pin_Bomba, 0)   # Esse e o unico que trabalha com logica correta

print("All_OFF")
