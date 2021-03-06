#!/usr/bin/env python
# encoding: utf-8
from audio import *
from random import randint 
from malib import *

#===============Fonctions===================
def analyseInterval(ying):
    global z, check, attack, interval, laNote
    pit = 0
    p = range(12)
    for i in range(12):
        p[i] = ying.get()
        print p[i]
        time.sleep(0.005)
        pit += p[i]
    pit /= 6    
    octave = midiToHz(laNote[interval[z]])
    #print "pit = %d and m = %d" % (pit, m)
    attack = True
    for m in octave:
        if m > pit*0.94 and m < pit*1.06: #0.97 et 1.03 est la valeur � mi-chemin entre deux demitons
            check = True
            
def pigeInterval(): #Fonction pour la pige de note en MIDI
    global interval,x,y,z
    x = random.choice(notePool)
    y = random.choice(settingsPool)+1   
    
    tuning = getTuning()
    relative = getRelative()
    
    if x == 0: #On affiche la note � jouer
        localText = "C"
    elif x == 1:
        localText = "C#/Db"
    elif x == 2:
        localText = "D"
    elif x == 3:
        localText = "D#/Eb"
    elif x == 4:
        localText = "E"
    elif x == 5:
        localText = "F"
    elif x == 6:
        localText = "F#/Gb"
    elif x == 7:
        localText = "G"
    elif x == 8:
        localText = "G#/Ab"
    elif x == 9:
        localText = "A"
    elif x == 10:
        localText = "A#/Bb"
    elif x == 11:
        localText = "B"
    if y == 1: #On affiche la note � jouer
        localText2 = "Minor 2nd" 
    elif y == 2:
        localText2 = "Major 2nd"
    elif y == 3:
        localText2 = "Minor 3rd"
    elif y == 4:
        localText2 = "Major 3rd"
    elif y == 5:
        localText2 = "Perfect 4th"
    elif y == 6:
        localText2 = "Augmented 4th"
    elif y == 7:
        localText2 = "Perfect 5th"
    elif y == 8:
        localText2 = "Minor 6th"
    elif y == 9:
        localText2 = "Major 6th"
    elif y == 10:
        localText2 = "Minor 7th"
    elif y == 11:
        localText2 = "Major 7th"
        
    if relative == 1: #Standard relative
        if (x + tuning) < 0:
            x = x+12+tuning
        else:
            x += tuning

    if (x+y)>=12: 
        y = x+y-12
    else:
        y += x
    interval[0] = x       
    interval[1] = y
    z = 0 #On reset le compteur de notes
    print "x = %i" % x
    return interval, localText, localText2
            
def testInterval():
    global interval, check, attack, z
    if attack is True:
        if check == True and z == 1:
            localResult = "BRAVO!"
            print localResult
            z = 0
            check = False
            attack = False
            pigeInterval()
            return localResult
        elif check == True:
            localResult = "CHECK!"
            print localResult
            z += 1
            print z
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
            
