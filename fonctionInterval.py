#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from random import randint 
from malib import *

#===============Fonctions===================
def analyseInterval():
    global z, check, attack, interval, laNote
    pit = 0
    p = range(24)
    for i in range(24):
        p[i] = ying.get()
        print p[i]
        time.sleep(0.001)
        pit += p[i]
    pit /= 12
    print pit      
    octave = midiToHz(laNote[interval[z]])
    #print "pit = %d and m = %d" % (pit, m)
    attack = True
    for m in octave:
        if m > pit*0.94 and m < pit*1.06: #0.97 et 1.03 est la valeur à mi-chemin entre deux demitons
            check = True
            
def pigeInterval(): #Fonction pour la pige de note en MIDI
    global interval,x,y,z
    x = random.randint(0,11)
    y = random.randint(1,11)    
    if x == 0: #On affiche la note à jouer
        print "C" 
        localText = "C"
    elif x == 1:
        print "C#/Db"
        localText = "C#/Db"
    elif x == 2:
        print "D"
        localText = "D"
    elif x == 3:
        print "D#/Eb"
        localText = "D#/Eb"
    elif x == 4:
        print "E"
        localText = "E"
    elif x == 5:
        print "F"
        localText = "F"
    elif x == 6:
        print "F#/Gb"
        localText = "F#/Gb"
    elif x == 7:
        print "G"
        localText = "G"
    elif x == 8:
        print "G#/Ab"
        localText = "G#/Ab"
    elif x == 9:
        print "A"
        localText = "A"
    elif x == 10:
        print "A#/Bb"
        localText = "A#/Bb"
    elif x == 11:
        print "B"
        localText = "B"
    if y == 1: #On affiche la note à jouer
        print "minor 2nd" 
        localText += "minor 2nd" 
    elif y == 2:
        print "major 2nd"
        localText += "major 2nd"
    elif y == 3:
        print "minor 3rd"
        localText += "minor 3rd"
    elif y == 4:
        print "major 3rd"
        localText += "major 3rd"
    elif y == 5:
        print "perfect 4th"
        localText += "perfect 4th"
    elif y == 6:
        print "augmented 4th"
        localText += "augmented 4th"
    elif y == 7:
        print "perfect 5th"
        localText += "perfect 5th"
    elif y == 8:
        print "minor 6th"
        localText += "minor 6th"
    elif y == 9:
        print "major 6th"
        localText += "major 6th"
    elif y == 10:
        print "minor 7th"
        localText += "minor 7th"
    elif y == 11:
        print "major 7th"
        localText += "major 7th"
        
    if (x+y)>12:
        y = x+y-12
    else:
        y += x
    interval[0] = x       
    interval[1] = y
    print interval    
    return interval, localText
            
def testInterval():
    global interval, check, attack, z
    if attack is True:
        if check == True and z == 1:
            print "BRAVO!"
            z = 0
            check = False
            attack = False
            pigeInterval()
        elif check == True:
            print "CHECK!"
            z += 1
            check = False
            attack = False
        elif check == False:
            print "RECOMMENCEZ!"
            z = 0
            attack = False
            check = False

