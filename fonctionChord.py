#!/usr/bin/env python
# encoding: utf-8
from random import *
from malib import *
from audio import *

#===============Fonctions===================
def analyseChord(ying):
    global z, check, attack, chord, laNote
    pit = 0
    p = range(12)
    for i in range(12):
        p[i] = ying.get()
        time.sleep(0.005)
        pit += p[i]
    pit /= 6      
    octave= midiToHz(laNote[chord[z]])
    attack = True
    for m in octave:
        if m > pit*0.94 and m < pit*1.06: #0.97 et 1.03 est la valeur à mi-chemin entre deux demitons
            check = True
            
def pigeChord(): #Fonction pour la pige de note en MIDI
    global chordType,x,y,z,chord, localText, localText2, chordHint, setHint
    x = random.choice(notePool)
    y = random.choice(settingsPool)
    i = random.randint(0,1)    
    
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
        localText2 = "Maj" 
    elif y == 1:
        localText2 = "Min"
    elif y == 2:
        localText2 = "Aug"
    elif y == 3:
        localText2 = "Dim"
    elif y == 4:
        localText2 = "Maj 7th"
    elif y == 5:
        localText2 = "Dom 7th" 
    elif y == 6:
        localText2 = "mMaj 7th"
    elif y == 7:
        localText2 = "mMin 7th"
    elif y == 8:
        localText2 = "Maj 6th"
    elif y == 9:
        localText2 = "Min 6th"
    elif y == 10:
        localText2 = "Sus 2"
    elif y == 11:
        localText2 = "Sus 4"
    
    #On calcule les notes faisant partie de l'accord
    chord[0] = x
    if (chord[0]+chordType[y][1]) >= 12: #On calcule la tierce
        chord[1] = chord[0]+chordType[y][1]-12
    else:
        chord[1] = chord[0]+chordType[y][1]
        
    if (chord[0]+chordType[y][2]) >= 12: #On calcule la quinte
        chord[2] = chord[0]+chordType[y][2]-12
    else:
        chord[2] = chord[0]+chordType[y][2]
        
    if (chord[0]+chordType[y][3]) >= 12:
        if chordType[y][3] != 0: #On calcule l'octave ou la septieme
            chord[3] = chord[0]+chordType[y][3]-12        
    elif chordType[y][3] != 0:
        chord[3] = chord[0]+chordType[y][3]
    else:
        chord[3] = chord[0]
        
    #On affiche la structure de l'accord    
    if i == 0: #On garde la structure standard
        localText += "\nC/G shape"
    elif i == 1: #On utilise la structure 1-5-7/8-3
        shape = []
        shape.append(chord[0])
        shape.append(chord[2])
        shape.append(chord[3])
        shape.append(chord[1])
        chord = shape
        localText += "\nA/E/D shape"
        
    z = 0 #On reset le compteur de notes
    return chord, localText, localText2, y
            
def testChord():
    global check, attack, z
    if attack is True:
        if check == True and z == 3:
            localResult = "BRAVO!"
            print localResult
            z = 0
            check = False
            attack = False
            pigeChord()
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

