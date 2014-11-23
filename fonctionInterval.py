#!/usr/bin/env python
# encoding: utf-8
from audio import *
from random import randint 
from malib import *

#===============Fonctions===================
def analyseInterval():
    global z, check, attack, interval, laNote
    pit = 0
    p = range(24)
    for i in range(24):
        p[i] = audio.ying.get()
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
    if y == 1: #On affiche la note à jouer
        localText += " minor 2nd" 
    elif y == 2:
        localText += " major 2nd"
    elif y == 3:
        localText += " minor 3rd"
    elif y == 4:
        localText += " major 3rd"
    elif y == 5:
        localText += " perfect 4th"
    elif y == 6:
        localText += " augmented 4th"
    elif y == 7:
        localText += " perfect 5th"
    elif y == 8:
        localText += " minor 6th"
    elif y == 9:
        localText += " major 6th"
    elif y == 10:
        localText += " minor 7th"
    elif y == 11:
        localText += " major 7th"
        
    if (x+y)>12:
        y = x+y-12
    else:
        y += x
    interval[0] = x       
    interval[1] = y
    print interval 
    print localText   
    return interval, localText
            
def testInterval():
    global interval, check, attack, z
    if attack is True:
        print "att"
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

