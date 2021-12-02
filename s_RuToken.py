import sys
import pyp11
import time

def ini_lib_RuToken():
    # Библиотека для eTokena
    # lib = 'd:\kurs\RuTokenAkt\eToken.dll'
    # Библиотека для RuTokena
    lib = 'd:\kurs\RuTokenAkt\\rtPKCS11.dll'
    # Загружаем библиотеку
    return (pyp11.loadmodule(lib))

def survey_RuToken(libid):
    slots = pyp11.listslots(libid)  #Загружаем список слотов
    num_slots = len(slots)
    tokpr = 0
    ser_num = '000000'
    i = 1
#Перебираем слоты
    for v in slots:
        flags = v[2]
#Проверяем наличие в стоке токена
        if (flags.count('TOKEN_PRESENT') !=0):
            tokpr = 1
            lab = v[1].strip()
            infotok = v[3]
            slotid = v[0]
#            print("Слот № "+ str(v[0]))
#            print("Метка токена в слоте: "+ v[1])
#            print("Инфа: " + infotok[0])
#            print("Инфа1: " + infotok[1])
#            print("Инфа2: " + infotok[2])
#            print("Инфа3: " + infotok[3])
            ser_num = infotok[3]
            break
    return(ser_num)
