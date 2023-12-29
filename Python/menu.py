# -*- coding: utf-8 -*-

import os
import subprocess

while True:
    # Limpa a tela e monta o "menu"
    os.system('clear')
    print('*** MENU PRINCIPAL ***\n')
    print('1. Ventilador   [ ON ]')
    print('2. Ventilador   [ OFF ]')
    print('3. Painel Umido [ ON ]')
    print('4. Painel Umido [ OFF ]')
    print('5. Fogger       [ ON ]')
    print('6. Fogger       [ OFF ]')
    print('7. Irrigacao    [ ON ]')
    print('8. Irrigacao    [ OFF ]')
    print('0. Sair...\n')
    
    a = input('Escolha uma opção: ')

    if (int(a)==0):
        os.system('clear')
        exit()
    if (int(a)==1):
        subprocess.call("python /var/www/html/atuadores/vent_ON.py", shell=True)

