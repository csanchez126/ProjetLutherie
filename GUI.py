#!/usr/bin/env python
# encoding: utf-8

import wx, os, time
from audio import *
from malib import *
from fonctionInterval import *
from fonctionEADGBE import *
from fonctionPige import *
from fonctionChord import *

#=========================GUI===============================
class MyFrame(wx.Frame):
    def __init__(self, parent, title, pos, size):
        wx.Frame.__init__(self, parent, id=-1, title=title, pos=pos, size=size)
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("#DDDDDD")

        self.audio = Audio(self)
        
        self.onOffText = wx.StaticText(self.panel, id=-1, label="Audio", 
                                       pos=(28,10), size=wx.DefaultSize)
        self.onOff = wx.ToggleButton(self.panel, id=-1, label="on / off", 
                                     pos=(10,28), size=wx.DefaultSize)
        self.incZ = wx.ToggleButton(self.panel, id=-1, label="Attack/Analyse", 
                                     pos=(10,150), size=wx.DefaultSize)
        

        # Un event du toggle appelle la methode self.handleAudio
        self.onOff.Bind(wx.EVT_TOGGLEBUTTON, self.handleAudio)
        self.incZ.Bind(wx.EVT_TOGGLEBUTTON, self.plusOne)
        
        # os.listdir(path) retourne tous les fichiers dans le dossier "path"
        # os.getcwd() retourne le repertoire courant.
        scripts = ["fonctionEADGBE.py", "fonctionChord.py", "fonctionInterval.py", "fonctionPige.py"]

        self.popupText = wx.StaticText(self.panel, id=-1, 
                    label="Choisir un test...", pos=(10,60), size=wx.DefaultSize)
        self.popup = wx.Choice(self.panel, id=-1, pos=(8,78), 
                               size=wx.DefaultSize, choices=scripts)
                            
        self.popup.Bind(wx.EVT_CHOICE, self.setTest)
        
        cb1 = wx.CheckBox(self.panel, -1, "E", (400, 40), (150, 20), wx.NO_BORDER)
        cb2 = wx.CheckBox(self.panel, -1, "B",(400, 60), (150, 20), wx.NO_BORDER)
        cb3 = wx.CheckBox(self.panel, -1, "G",(400, 80), (150, 20), wx.NO_BORDER)
        cb4 = wx.CheckBox(self.panel, -1, "D", (400, 100), (150, 20), wx.NO_BORDER)
        cb5 = wx.CheckBox(self.panel, -1, "A",(400, 120), (150, 20), wx.NO_BORDER)
        cb6 = wx.CheckBox(self.panel, -1, "E",(400, 140), (150, 20), wx.NO_BORDER)
        
        cbC = wx.CheckBox(self.panel, -1, "C", (200, 300), (30, 20), wx.NO_BORDER)
        cbCsDb = wx.CheckBox(self.panel, -1, "C#/Db",(240, 300), (30, 20), wx.NO_BORDER)
        cbD = wx.CheckBox(self.panel, -1, "D",(280, 300), (30, 20), wx.NO_BORDER)
        cbDsEb = wx.CheckBox(self.panel, -1, "D#/Eb", (320, 300), (30, 20), wx.NO_BORDER)
        cbE = wx.CheckBox(self.panel, -1, "E",(360, 300), (30, 20), wx.NO_BORDER)
        cbF = wx.CheckBox(self.panel, -1, "F",(400, 300), (30, 20), wx.NO_BORDER)
        cbFsGb = wx.CheckBox(self.panel, -1, "F#/Gb", (440, 300), (30, 20), wx.NO_BORDER)
        cbG = wx.CheckBox(self.panel, -1, "G",(480, 300), (30, 20), wx.NO_BORDER)
        cbGsAb = wx.CheckBox(self.panel, -1, "G#/Ab",(520, 300), (30, 20), wx.NO_BORDER)
        cbA = wx.CheckBox(self.panel, -1, "A", (560, 300), (30, 20), wx.NO_BORDER)
        cbAaBb = wx.CheckBox(self.panel, -1, "A#/Bb",(600, 300), (30, 20), wx.NO_BORDER)
        cbB = wx.CheckBox(self.panel, -1, "B",(640, 300), (30, 20), wx.NO_BORDER)
    
        #Boite de texte 
        self.l5 = wx.StaticText(self.panel, id=-1, label="Test Positions", pos=(230,10), size=wx.DefaultSize)
        self.t5 = wx.TextCtrl(self.panel, -1,"0123456789\n", pos=(230,30),size=(150, 50),
                      style = wx.TE_MULTILINE
                         #| wx.TE_RICH
                         | wx.TE_RICH2
                         )
        
    def plusOne(self, evt):
        global attack, check
        if evt.GetInt() == 1 or evt.GetInt() == 0:
            attack = True
            check = True
            
    def handleAudio(self, evt):
        # evt.GetInt() retourne 1 si le toggle est a on, 0 s'il est a off
        if evt.GetInt() == 1:
            s.start()
        else:
            s.stop()

    def setTest(self, evt): 
        global functionChoice
        print evt.GetString()
        functionChoice = evt.GetString()
        self.t5.Clear()
        self.t5.WriteText(evt.GetString())
        
        if evt.GetString() == "fonctionEADGBE.py":
            EADGBEFunc = pigeEADGBE()
            text = EADGBEFunc[1]
            print text
            self.t5.Clear()
            self.t5.WriteText(text)
            self.audio.setTest(testEADGBE)
            self.audio.setAnalyse(analyseEADGBE)
            
        elif evt.GetString() == "fonctionInterval.py":
            intervalFunc = pigeInterval()
            text = intervalFunc[1]
            print text
            self.t5.Clear()
            self.t5.WriteText(text)
            self.audio.setTest(testInterval)
            self.audio.setAnalyse(analyseInterval)

        elif evt.GetString() == "fonctionChord.py":
            chordFunc = pigeChord()
            text = chordFunc[1]
            print text
            self.t5.Clear()
            self.t5.WriteText(text)
            self.audio.setTest(testChord)
            self.audio.setAnalyse(analyseChord)      
        #Reste la fonction pige a reviser

    def loopTest(self):
        global functionChoice
        self.t5.Clear()
        self.t5.WriteText(functionChoice)
        self.audio.setTest(functionChoice)
        self.audio.setAnalyse(functionChoice)
    
    def printTextBox(self, text):
        self.t5.WriteText("\n")
        self.t5.WriteText(text)
        
        
        
    
app = wx.App(False)
mainFrame = MyFrame(None, title='Simple App', pos=(100,100), size=(800,600))
mainFrame.Show()
app.MainLoop()