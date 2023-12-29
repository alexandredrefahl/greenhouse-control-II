#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Programa: Le os sensores e toma as decisoes baseadas nos valores lidos
# Autor: Alexandre Drefahl
 
# Carrega as bibliotecas
import RPi.GPIO as GPIO
import time
import datetime
import csv
import sys
import os.path
import bme280           # Sensor de Temperatura umidade e pressao
import bh1750           # Sensor de Luminosidade
import I2C_LCD_driver   # Funcoes relativas ao LCD
import socket
import requests
#import MySQLdb
 
try:
   (chip_id, chip_version) = bme280.readBME280ID()
   print "*** DADOS dos Sensores \n"
   print "Chip ID :", chip_id
   print "Versao  :", chip_version
   print "\n"
except:
   print "Nao foi possivel conectar ao sensor de temperatura e umidade"

#Define os Pinos

#Atuadores
pin_Fotoperiodo = 26
pin_Irriga = 35
pin_Fogger = 36
pin_Painel = 38
pin_Ventilador = 40

#Sensores
pin_Chuva = 15
#pin_Data_DHT = 25

# Modo BCM = GPIOx // Modo BOARD = Numero do pino
GPIO.setmode(GPIO.BOARD)
#Desliga os avisos do compilador
GPIO.setwarnings(False)

#Direcao dos pinos
GPIO.setup(pin_Chuva, GPIO.IN)
GPIO.setup(pin_Painel, GPIO.OUT)
GPIO.setup(pin_Ventilador, GPIO.OUT)
GPIO.setup(pin_Fogger, GPIO.OUT)
GPIO.setup(pin_Fotoperiodo, GPIO.OUT)
GPIO.setup(pin_Irriga, GPIO.OUT)

# Define o nome dos arquivos automaticos para indicar o status dos botoes e definir os atuadores
caminho = "/var/www/html/"
lockVentilador = "ventAUTO.txt"
lockFogger = "foggAUTO.txt"
lockPainel = "painelAUTO.txt"
lockFotoperiodo = "fotopAUTO.txt"
lockIrriga = "irrigaAUTO.txt"

#Define os Parametros de Umidade e Temperatura Máximos
#Temp_MAX = 39      # Em Graus
#Temp_OFF = 37.1    # Em Graus
Temp_MAX = 55	    # Sensor com alteracao na leitura
Temp_OFF = 47	    # Sensor com alteração na leitura
Umid_MIN = 65       # Em Percentual
Lux_MIN = 5000      # Em lux
Tempo_LOG = 5       # Em minutos
Hora_INI = 07
Hora_FIM = 19

# Informacoes iniciais
print ("*** Lendo SENSORES\n")
 
# Efetua a leitura do sensor
print("   Lendo Temperatura, Umidade e Pressao [BME-280]")
try:
   temp,press,umid = bme280.readBME280All()
except:
   temp = 0
   press = 0
   umid = 0

# Efetua a leitura de Luminosidade
print("   Lendo Luminosidade [BH-1750]\n")
try:
   lumen = bh1750.readLight()
except:
   lumen = 0

print("*** Dados brutos...\n")
print "Temperatura : ", temp, "C"
print "Pressao : ", press, "hPa"
print "Umidade : ", umid, "%"
print "Luminosidade: " + str(lumen) + " lx"
print "\n"

# Caso leitura esteja ok, mostra os valores na tela
if umid is not None and temp is not None:
    print("*** Dados formatados...\n")
    print ("   Temperatura = {0:0.1f}C\n   Umidade = {1:0.1f}%\n   Pressao = {2:0.1f}hPa").format(temp, umid, press)
    varChuva = GPIO.input(pin_Chuva)
    if pin_Chuva:
        print("   Sensor de Chuva: Tempo seco")
    else:
        print("   Sensor de Chuva: Chovendo")
    
    print("\n*** Definindo ATUADORES\n")

# Os pinos do Raspberry trabalham com logica invertida
    if os.path.isfile(caminho + lockVentilador):
        print("VENTILADOR em modo Automatico")
        if temp > Temp_MAX:
            print("   Temperatura alta: acionando Ventilacao")
            GPIO.output(pin_Ventilador,0)		#Liga o Ventilador
	    if os.path.isfile(caminho + lockPainel):
                GPIO.output(pin_Painel,0)
	if temp < Temp_OFF:
            print("   Temperatura normalizada: Ventilacao desligada")
            GPIO.output(pin_Ventilador,1)		#Desliga o Ventilador
            GPIO.output(pin_Painel,1)
    if os.path.isfile(caminho + lockFogger):
        print("FOGGER em modo Automatico")
        if umid < Umid_MIN:
            #Determina um tempo maior quanto menor for a umidade relativa
            tempo=10        #Segundos de atuacao do Fogger (Tempo Base)
            if umid < 30:
                tempo = 40  #40 segundos
            if umid > 30 and umid < 40:
                tempo = 30  #30 segundos
            if umid > 40 and umid < 50:
                tempo = 10  #20 segundos
            if umid > 50 and umid < 60:
                tempo = 7  #10 segundos de spray
            print("   Acionando Fogger por "+ str(tempo) + " segundos")
            GPIO.output(pin_Fogger,0)		#Liga o Fogger
            time.sleep(tempo)
            GPIO.output(pin_Fogger,1)		#Desliga o Fogger
        else:
            print("   Umidade dentro da faixa desejada...")
else:
   # Mensagem de erro de comunicacao com o sensor
   print("Falha ao ler dados do sensor de Temperatura/Umidade")

# Pega a hora no formato 24h
hora = int(time.strftime('%H'))

if os.path.isfile(caminho + lockFotoperiodo):
    print("Fotoperiodo em modo Automatico")
    if hora >= Hora_INI and hora < Hora_FIM and lumen < Lux_MIN:
        GPIO.output(pin_Fotoperiodo,0)		#Liga o Fotoperiodo
        print("Fotoperiodo Ligado...")
    else:
        GPIO.output(pin_Fotoperiodo,1)		#Desliga o Fotoperiodo
        print("Fotoperiodo Desligado...")


#############################################################
#
#    Grava os dados no arquivo 
#
#############################################################

print("\n*** REGISTRANDO dados no arquivo")

# Gera Timestamp
ts = time.localtime()
varHora = time.strftime("%d-%m-%Y %H:%M:%S", ts)

# MOSTRA OS DADOS NO LCD
try:
    lcdi2c = I2C_LCD_driver.lcd()
    lcdi2c.lcd_display_string("T:{0:0.1f}C  U:{1:0.1f}%".format(temp, umid), 1,0)
    lcdi2c.lcd_display_string("L:{0:0.1f}lx".format(lumen), 2,0)
    lcdi2c.lcd_display_string(time.strftime("%H:%M", ts), 2,11)
except Exception:
    print("Erro no display LCD, ignorando etapa...\n")

# Povoa as variaveis dos sensores
varTemp = "{0:.1f}".format(temp)
varUmid = "{0:.1f}".format(umid)
varPres = "{0:.1f}".format(press)
varLume = "{0:.1f}".format(lumen)

# Povoa as variaveis com os status dos pinos
# Lido diretamente do "arquivo" do pino

# Pino 40 ou GPIO-21 = VENTILADOR
fv = open("/sys/class/gpio/gpio21/value","r")
stVentilador = fv.read(1)
fv.close()
# Pino 38 ou GPIO-20 = PAINEL UMIDO
fv = open("/sys/class/gpio/gpio20/value","r")
stPainel = fv.read(1)
fv.close()
# Pino 35 ou GPIO-19 = IRRIGACAO
fv = open("/sys/class/gpio/gpio19/value","r")
stIrriga = fv.read(1)
fv.close()
# Pino 36 ou GPIO-16 = FOGGER
fv = open("/sys/class/gpio/gpio16/value","r")
stFogger = fv.read(1)
fv.close()
# Pino 32 ou GPIO-12 = FOTOPERIODO (Vai mudar)
#fv = open("/sys/class/gpio/gpio12/value","r")
#stFotoperiodo = fv.read(1)
stFotoperiodo = 0
#fv.close()

# Se os aquivos de Lock estiverem presentes, devolve modo automatico
if os.path.isfile(caminho + lockVentilador):
    btVentilador = 3
else:
    btVentilador = stVentilador

if os.path.isfile(caminho + lockFogger):
    btFogger = 3
else:
    btFogger = stFogger

if os.path.isfile(caminho + lockPainel):
    btPainel = 3
else:
    btPainel = stPainel

if os.path.isfile(caminho + lockFotoperiodo):
    btFotoperiodo = 3
else:
    btFotoperiodo = stFotoperiodo

if os.path.isfile(caminho + lockIrriga):
    btIrriga = 3
else:
    btIrriga = stIrriga

# Reune tudo em uma lista
myList = [varTemp, varUmid, varLume, varPres, varChuva, varHora, stVentilador, stPainel, stFogger, stFotoperiodo, stIrriga ,btVentilador, btFogger, btPainel, btFotoperiodo, btIrriga]

# Grava o arquivo que vai fazer a "ponte"   
f = open('/var/www/html/leitura.csv', 'wt')

# Grava o arquivo de log dos dados
fl = open('/var/www/html/registro.csv',"a+")

# Faz a gravacao em disco
try:
    writer = csv.writer(f,quoting=csv.QUOTE_MINIMAL)
    writer.writerow(myList)
finally:
    f.close()

min = int(datetime.datetime.now().strftime("%M"))

if (min % Tempo_LOG == 0):
    # Faz a gravaçao do registro
    try:
        writer = csv.writer(fl,quoting=csv.QUOTE_MINIMAL)
        writer.writerow(myList)
    finally:
        fl.close()
