#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from random import randint 
from malib import *

#===============Fonctions===================
def analyseNote(ying):
    global x, y, laNote, attack, check
    pit = 0
    p = range(12)
    for i in range(12):
        p[i] = ying.get()
        time.sleep(0.02)
        pit += p[i]
    pit /= 6      
    octave= midiToHz(laNote[x])
    #print "pit = %d and m = %d" % (pit, octave[3])
    attack = True
    for m in octave:
        if m > pit*0.94 and m < pit*1.06: #0.97 et 1.03 est la valeur à mi-chemin entre deux demitons
            check = True
            
def pigeNote(): #Fonction pour la pige de note en MIDI
    global laNote,x,y,z
    x = random.randint(0,11)
    y = random.randint(0,7)
    
    if x == 0: #On affiche la note à jouer
        localText = "Play any C"
    elif x == 1:
        localText = "Play any C#"
    elif x == 2:
        localText = "Play any D"
    elif x == 3:
        localText = "Play any D#/Eb"
    elif x == 4:
        localText = "Play any E"
    elif x == 5:
        localText = "Play any F"
    elif x == 6:
        localText = "Play any F#/Gb"
    elif x == 7:
        localText = "Play any G"
    elif x == 8:
        localText = "Play any G#/Ab"
    elif x == 9:
        localText = "Play any A"
    elif x == 10:
        localText = "Play any A#/Bb"
    elif x == 11:
        localText = "Play any B"
    #print localText
    z=0
    return x, localText
        
def testNote():
    global check, attack, z
    if attack is True:
        if check == True:
            localResult = "BRAVO!"
            print localResult
            z = 0
            check = False
            attack = False
            pigeNote()
            return localResult
        elif check == False:
            localResult = "RECOMMENCEZ!"
            print localResult
            z = 0
            attack = False
            check = False
            return localResult  
            


