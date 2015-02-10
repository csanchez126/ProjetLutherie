#=============Variable globales================

#Notes midi sur chaque octave audible de la guitare
C     = [12, 24, 36, 48, 60, 72, 84, 96]    
CsDb= [13, 25, 37, 49, 61, 73, 85, 97]    
D      = [14, 26, 38, 50, 62, 74, 86, 98]
DsEb = [15, 27, 39, 51, 63, 75, 87, 99]
E       = [16, 28, 40, 52, 64, 76, 88, 100]
F       = [17, 29, 41, 53, 65, 77, 89, 101]
FsGb  = [18, 30, 42, 54, 66, 78, 90, 102]
G      = [19, 31, 43, 55, 67, 79, 91, 103]
GsAb = [20, 32, 44,56, 68, 80, 92, 104]
A      = [21, 33, 45, 57, 69, 81, 93, 105]
AsBb = [22, 34, 46, 58, 70, 82, 94, 106]
B      = [23, 35, 47, 59, 71, 83, 95, 107]
laNote = [C, CsDb, D, DsEb, E, F, FsGb, G, GsAb, A, AsBb, B] #Pour la pige de notes
key = [0,0]

#Positions pour le test EADBGBE
pos0 = [E[2],A[2],D[3],G[3],B[3],E[4]] #Fret 0  
pos1 = [G[2],B[2],E[3],A[3],D[4],G[4]] #Fret 3
pos2 = [A[2],D[3],G[3],B[3],E[4],A[4]] #Fret 5
pos3 = [B[2],E[3],A[3],D[4],G[4],B[4]] #Fret 7
pos4 = [D[3],G[3],B[3],E[4],A[4],D[5]] #Fret 10
pos5 = [E[3],A[3],D[4],G[4],B[4],E[5]] #Fret 12
position = [pos0, pos1, pos2, pos3, pos4, pos5]

#Listes pour le test des accords
maj = [0, 4, 7, 0]  #1,3,5,1
min = [0, 3, 7, 0]  #1,3b,5,1
aug = [0, 4, 8, 0]  #1,3,5#,1
dim = [0, 3, 6, 0]  #1,3b,5b,1
maj7 = [0,4,7,11] #1,3,5,7
min7 = [0,3,7,10] #1,3b,5,7b
chordType = [maj, min, aug, dim, maj7, min7]
shape = [0,0,0,0]
chord = [0,0,0,0] #Liste pour les notes de l'accord

x = 0 #Variable pour la note a piger 
y = 0 #Variable pour l'octave de la note pigee
z = 0 #Variable pour la corde a jouer
attack = False # Variable pour valider une attaque
check = False #Variable pour valider la note jouee
noteOk = False #Variable pour valider la note jouee
interval = [0,0] #Variable pour l'intervale: premiere valeur = tonalite, la seconde = l'equart
notePool = [1,1,1,1,1,1,1,1,1,1,1,1]
settingsPool = [1,1,1,1,1,1,1,1,1,1]

