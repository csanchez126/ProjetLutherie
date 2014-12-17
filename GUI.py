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
        self.chosenTest = None
        self.chosenPige = None
        self.chosenAnalyse = None
        self.fonctionPige = None
        
        self.onOffText = wx.StaticText(self.panel, id=-1, label="Audio", 
                                       pos=(10,10), size=wx.DefaultSize)
        self.onOff = wx.ToggleButton(self.panel, id=-1, label="on / off", 
                                     pos=(10,28), size=wx.DefaultSize)
        self.incZ = wx.ToggleButton(self.panel, id=-1, label="Attack/Analyse", 
                                     pos=(10,150), size=wx.DefaultSize)

        # Un event du toggle appelle la methode self.handleAudio
        self.onOff.Bind(wx.EVT_TOGGLEBUTTON, self.handleAudio)
        self.incZ.Bind(wx.EVT_TOGGLEBUTTON, self.plusOne)
        
        # os.listdir(path) retourne tous les fichiers dans le dossier "path"
        # os.getcwd() retourne le repertoire courant.
        scripts = ["EADGBE Sequence", "Chord Test", "Interval Test", "Random Note"]

        self.popupText = wx.StaticText(self.panel, id=-1, 
                    label="Tests:", pos=(10,60), size=wx.DefaultSize)
        self.popup = wx.Choice(self.panel, id=-1, pos=(10,78), 
        
                               size=wx.DefaultSize, choices=scripts)
                            
        self.popup.Bind(wx.EVT_CHOICE, self.setTest)
        """
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
        """
        self.testPos = wx.StaticText(self.panel, id=-1, label="Test Positions", pos=(160,10), size=wx.DefaultSize)
        self.testDesc = wx.StaticText(self.panel, id=-1, label="Test Description:", pos=(10,255), size=wx.DefaultSize)
        
        self.textbox1 = wx.TextCtrl(self.panel, -1,"Please chose a test!", pos=(160,30),size=(375, 100),
                      style = wx.TE_MULTILINE
                         #| wx.TE_RICH
                         | wx.TE_RICH2
                         )
        self.fontColor1(30, wx.NullColour)
        
        self.textbox2 = wx.TextCtrl(self.panel, -1," ", pos=(160,150),size=(375, 100),
                      style = wx.TE_MULTILINE
                         #| wx.TE_RICH
                         | wx.TE_RICH2
                         )
        
        self.textbox3 = wx.TextCtrl(self.panel, -1," ", pos=(10,275),size=(525, 120),
                      style = wx.TE_MULTILINE
                         #| wx.TE_RICH
                         | wx.TE_RICH2
                         )
        
        self.descPige = "User must play the randomly selected note on any octave."
        self.descInterval = "User must play the selected interval in an ascending order, starting from the randomly selected note"
        self.descChord = "User must play the four notes of the selected chord in an ascending order. The shape refers to the structure of the open chord shapes."
        self.descEADGBE = "User must play the standard tuning sequence at the randomly selected fret, starting from the lowest string."
        
    def plusOne(self, evt):
        global attack, check
        if evt.GetInt() == 1 or evt.GetInt() == 0:
            setTrue()
        else:
            pass
            
    def handleAudio(self, evt):
        # evt.GetInt() retourne 1 si le toggle est a on, 0 s'il est a off
        if evt.GetInt() == 1:
            s.start()
        else:
            s.stop()

    def setTest(self, evt): 
        print evt.GetString()
        self.chosenPige = evt.GetString()
        self.textbox1.Clear()
        self.textbox1.WriteText(evt.GetString())
        
        if evt.GetString() == "EADGBE Sequence":
            self.fonctionPige = pigeEADGBE()
            text = self.fonctionPige[1]
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descEADGBE)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testEADGBE)
            self.audio.setAnalyse(analyseEADGBE)
            
        elif evt.GetString() == "Interval Test":
            self.fonctionPige = pigeInterval()
            text = self.fonctionPige[1]
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descInterval)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testInterval)
            self.audio.setAnalyse(analyseInterval)

        elif evt.GetString() == "Chord Test":
            self.fonctionPige = pigeChord()
            text = self.fonctionPige[1]
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descChord)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testChord)
            self.audio.setAnalyse(analyseChord)      
            
        elif evt.GetString() == "Random Note":
            self.fonctionPige = pigeNote()
            text = self.fonctionPige
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descPige)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testNote)
            self.audio.setAnalyse(analyseNote)  
            
    def loopTest(self):
        if  self.chosenPige == "EADGBE Sequence":
            self.fonctionPige = pigeEADGBE()
            text = self.fonctionPige[1]
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descEADGBE)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testEADGBE)
            self.audio.setAnalyse(analyseEADGBE)
            
        elif self.chosenPige == "Interval Test":
            self.fonctionPige = pigeInterval()
            text = self.fonctionPige[1]
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descInterval)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testInterval)
            self.audio.setAnalyse(analyseInterval)

        elif self.chosenPige == "Chord Test":
            self.fonctionPige = pigeChord()
            text = self.fonctionPige[1]
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descChord)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testChord)
            self.audio.setAnalyse(analyseChord)   
            
        elif self.chosenPige == "Random Note":
            self.fonctionPige = pigeNote()
            text = self.fonctionPige
            print text
            self.textbox1.Clear()
            self.textbox1.WriteText(text)
            self.fontColor1(30, wx.NullColour)
            self.textbox3.Clear()
            self.textbox3.WriteText(self.descPige)
            self.fontColor3(15, wx.NullColour)
            self.audio.setTest(testNote)
            self.audio.setAnalyse(analyseNote)  
            
    def printTextBox1(self, data):
        self.textbox1.WriteText("\n")
        self.textbox1.WriteText(data)
    
    def printTextBox2(self, data):
        self.textbox2.WriteText(data)
    
    def printTextBox3(self, data):
        self.textbox3.WriteText(data)
        
    def fontColor1(self, fontSize, color):
        font = wx.Font(fontSize, wx.DEFAULT, wx.NORMAL, wx.BOLD, False)
        self.textbox1.SetStyle(0, 40, wx.TextAttr(color, wx.NullColour, font))
        
    def fontColor2(self, fontSize, color):
        font = wx.Font(fontSize, wx.DEFAULT, wx.NORMAL, wx.BOLD, False)
        self.textbox2.SetStyle(0, 20, wx.TextAttr(color, wx.NullColour, font))
        
    def fontColor3(self, fontSize, color):
        font = wx.Font(fontSize, wx.DEFAULT, wx.NORMAL, wx.BOLD, False)
        self.textbox3.SetStyle(0, 300, wx.TextAttr(color, wx.NullColour, font))
        
        
app = wx.App(False)
mainFrame = MyFrame(None, title='FretMemo', pos=(100,100), size=(560,450))
mainFrame.Show()
app.MainLoop()