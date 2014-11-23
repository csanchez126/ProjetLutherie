#!/usr/bin/env python
# encoding: utf-8
from pyo import *
from random import randint 
from malib import *


#===============Fonctions===================
def analyseChord():
    global ying, z, check, attack, chord, laNote
    pit = 0
    p = range(24)
    for i in range(24):
        p[i] = audio.ying.get()
        time.sleep(0.001)
        pit += p[i]
    pit /= 12      
    octave= midiToHz(laNote[chord[z]])
    print "pit = %d and m = %d" % (pit, octave[3])
    attack = True
    for m in octave:
        if m > pit*0.94 and m < pit*1.06: #0.97 et 1.03 est la valeur à mi-chemin entre deux demitons
            check = True
            
def pigeChord(): #Fonction pour la pige de note en MIDI
    global chordType,x,y,z,chord,shape, localText
    x = random.randint(0,11)
    y = random.randint(0,5)
    z = random.randint(0,1)    
    
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
        
    #On affiche le type d'accord maj, min, aug, dim, maj7, min7
    if y == 0: 
        localText += " major" 
    elif y == 1:
        localText += " minor"
    elif y == 2:
        localText += " augmented"
    elif y == 3:
        localText += " diminished"
    elif y == 4:
        localText += " major 7th"
    elif y == 5:
        localText += " minor 7th" 
    
    #On calcule les notes faisant partie de l'accord
    chord[0] = x
    if (chord[0]+chordType[y][1])>12: #On calcule la tierce
        chord[1] = chord[0]+chordType[y][1]-12
    else:
        chord[1] += chordType[y][1]
        
    if (chord[0]+chordType[y][2])>12: #On calcule la quinte
        chord[2] = chord[0]+chordType[y][2]-12
    else:
        chord[2] += chordType[y][2]
        
    if (chord[0]+chordType[y][3])>12 and chordType[y][3] != 1: #On calcule l'octave ou la septieme
        chord[3] = chord[0]+chordType[y][3]-12        
    elif chordType[y][3] != 1:
        chord[3] += chordType[y][3]
    else:
        chord[3] = chord[0]
        
    #On affiche la structure de l'accord    
    if z == 0: #On garde la structure standard
        localText += "\nC/G shape"
    elif z == 1: #On utilise la structure 1-5-7/8-3
        shape = chord
        chord[0] = shape[0]
        chord[1] = shape[2]
        chord[2] = shape[3]
        chord[3] = shape[1]
        localText += "\nA/E/D shape"
                
    return chord, localText
            
def testChord():
    global chord, check, attack, z
    if attack is True:
        if check == True and z == 3:
            print "BRAVO!"
            z = 0
            check = False
            attack = False
            pigeChord()
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

