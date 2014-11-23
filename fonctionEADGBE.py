#!/usr/bin/env python
# encoding: utf-8
from audio import *
from random import randint 
from malib import *


#===============Fonctions===================
def analyseEADGBE():
    global ying, x, y, check, attack, position, z
    pit = 0
    p = range(24)
    for i in range(24):
        p[i] = audio.ying.get()
        time.sleep(0.001)
        pit += p[i]
    pit /= 12      
    m = midiToHz(position[x][z])
    print "pit = %d and m = %d" % (pit, m)
    attack = True
    if m > pit*0.93 and m < pit*1.06: #0.97 et 1.03 est la valeur � mi-chemin entre deux demitons
            check = True 
            
def pigeEADGBE(): #Fonction pour la pige de note en MIDI
    global x
    x = random.randint(0,5)
    if x == 0:
        localText = "Jouez la sequence aux cordes ouvertes"
    elif x == 1:
        localText = "Jouez la sequence a la 3eme case"
    elif x == 2:
        localText = "Jouez la sequence a la 5eme case"
    elif x == 3:
        localText = "Jouez la sequence a la 7eme case"
    elif x == 4:
        localText = "Jouez la sequence a la 10eme case"
    elif x == 5:
        localText = "Jouez la sequence a la 12eme case"
    return x, localText
 
def testEADGBE():
    global check, attack, z
    if attack is True:
        print z
        if check == True and z == 5:
            localResult = "BRAVO!"
            return localResult
            print localResult
            z = 0
            check = False
            attack = False
            pigeEADGBE()
        elif check == True:
            localResult = "CHECK!"
            return localResult
            print localResult
            z += 1
            check = False
            attack = False
        elif check == False:
            localResult = "RECOMMENCEZ!"
            return localResult
            print localResult
            z = 0
            attack = False
            check = False