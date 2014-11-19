#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from random import randint 
from malib import *



#===============Fonctions===================


def pige(): #Fonction pour la pige de note en MIDI
    global laNote,x,y
    x = random.randint(0,11)
    y = random.randint(0,7)
    
    #obj.Setvalue(string)
    
    if x == 0: #On affiche la note à jouer
        print "laNote[%i][%i] = C" % (x,y)
    elif x == 1:
        print "laNote[%i][%i] = C#" % (x,y)
    elif x == 2:
        print "laNote[%i][%i] = D" % (x,y)
    elif x == 3:
        print "laNote[%i][%i] = D#/Eb" % (x,y)
    elif x == 4:
        print "laNote[%i][%i] = E" % (x,y)
    elif x == 5:
        print "laNote[%i][%i] = F" % (x,y)
    elif x == 6:
        print "laNote[%i][%i] = F#/Gb" % (x,y)
    elif x == 7:
        print "laNote[%i][%i] = G" % (x,y)
    elif x == 8:
        print "laNote[%i][%i] = G#/Ab" % (x,y)
    elif x == 9:
        print "laNote[%i][%i] = A" % (x,y)
    elif x == 10:
        print "laNote[%i][%i] = A#/Bb" % (x,y)
    elif x == 11:
        print "laNote[%i][%i] = B" % (x,y)
    return laNote[x][y]

        
def analyse():
    global current, x, y, laNote
    pit = 0
    p = range(24)
    for i in range(24):
        p[i] = ying.get()
        time.sleep(0.005)
        pit += p[i]
        print p[i]
    pit /= 12      
    octave = midiToHz(laNote[x])
    attack = True
    for m in octave:
        if m > pit*0.94 and m < pit*1.06: #0.97 et 1.03 est la valeur à mi-chemin entre deux demitons
            print "BRAVO!"


