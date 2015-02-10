#!/usr/bin/env python
# encoding: utf-8
from audio import *
from random import randint 
from malib import *
import time

#===============Fonctions===================
def analyseEADGBE(ying):
    global x, y, check, attack, position, z
    pit = 0
    p = range(12)
    for i in range(12):
        p[i] = ying.get() # commes from the audio class.
        time.sleep(0.005)
        pit += p[i]
    pit /= 6      
    m = midiToHz(position[x][z])
    print "pit = %d and m = %d" % (pit, m)
    attack = True
    if m > pit*0.93 and m < pit*1.06: #0.97 et 1.03 est la valeur � mi-chemin entre deux demitons
            check = True 
            
def pigeEADGBE(): #Fonction pour la pige de note en MIDI
    global x, z
    x = random.randint(0,5)
    if x == 0:
        localText = "Play the open string sequence"
    elif x == 1:
        localText = "Play the sequence at the 3rd fret"
    elif x == 2:
        localText = "Play the sequence at the 5th fret"
    elif x == 3:
        localText = "Play the sequence at the 7th fret"
    elif x == 4:
        localText = "Play the sequence at the 10th fret"
    elif x == 5:
        localText = "Play the sequence at the 12th fret"
    z = 0 #On reset le compteur de notes
    return x, localText
 
def testEADGBE():
    global check, attack,z 
    if attack is True:
        if check == True and z == 5:
            localResult = "BRAVO!"
            print localResult
            z = 0
            check = False
            attack = False
            pigeEADGBE()
            return localResult
        elif check == True:
            localResult = "CHECK!"
            print localResult
            z += 1
            check = False
            attack = False
            return localResult
        elif check == False:
            localResult = "RECOMMENCEZ!"
            print localResult
            z = 0
            attack = False
            check = False
            return localResult            

            
def setTrue():
    global attack, check
    attack = True 
    check = True 