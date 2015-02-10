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
        self.chUncheckNotes = wx.ToggleButton(self.panel, id=600, label="Check/Uncheck All", pos=(10,290), size=wx.DefaultSize)
        self.chUncheckNotes.Bind(wx.EVT_TOGGLEBUTTON, self.checkUncheckAll)
        self.chUncheckSettings = wx.ToggleButton(self.panel, id=601, label="Check/Uncheck All", pos=(10,530), size=wx.DefaultSize)
        self.chUncheckSettings.Bind(wx.EVT_TOGGLEBUTTON, self.checkUncheckAll)
        
        #=========================MenuBar===============================
        self.menuBar = wx.MenuBar()
        self.menu1 = wx.Menu()
        self.menuTestNames = ["&EADGBE Sequence", "&Interval Test", "&Chord Test", "&Random Note"]
        for i in range (4):
            self.menu1.Append(i+100, self.menuTestNames[i],"")
            self.Bind(wx.EVT_MENU, self.setTest, id=i+100)
        self.menuBar.Append(self.menu1, "&Tests")
        self.SetMenuBar(self.menuBar)
        #========================Variables===============================
        self.audio = Audio(self)
        self.chosenTest = None
        self.chosenPige = None
        self.chosenAnalyse = None
        self.fonctionPige = None
        self.descPige = "User must play the randomly selected note on any octave."
        self.descInterval = "User must play the selected interval in an ascending order, starting from the randomly selected note"
        self.descChord = "User must play the four notes of the selected chord in an ascending order. The shape refers to the structure of the open chord shapes."
        self.descEADGBE = "User must play the standard tuning sequence at the randomly selected fret, starting from the lowest string."

        #==================================LABELS============================================
        self.testPos = wx.StaticText(self.panel, id=-1, label="Play:", pos=(190,10), size=wx.DefaultSize)
        self.testResult = wx.StaticText(self.panel, id=-1, label="Result:", pos=(370,10), size=wx.DefaultSize)
        self.testDesc = wx.StaticText(self.panel, id=-1, label="Description:", pos=(190,230), size=wx.DefaultSize)
        self.testNotes = wx.StaticText(self.panel, id=-1, label="Notes:", pos=(10,10), size=wx.DefaultSize)
        self.testSettings = wx.StaticText(self.panel, id=-1, label="Settings:", pos=(10,330), size=wx.DefaultSize)
        
        #================================TEXTBOXES============================================        
        self.textboxes = []
        self.tbPositions = [(190,30),(370,30),(190,250)]
        self.tbSizes = [(150,150),(150,150),(330,150)]
        ids = 2000
        for i in range(3):
            self.textboxes.append(wx.TextCtrl(self.panel, ids+i, pos=self.tbPositions[i], size=self.tbSizes[i], style = wx.TE_MULTILINE | wx.TE_RICH2))
            
        #================================CHECKBOXES============================================ 
        #---------------------------------NoteBoxes-------------------------------------------    
        self.noteBoxes = []
        self.noteNames = ["C","C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
        self.abs = 10
        self.ord = 35
        ids = 1000
        for i in range(12):
            if i in [0,2,4,5,7,9,11]:
                self.noteBoxes.append(wx.CheckBox(self.panel, ids+i, self.noteNames[i],(self.abs, self.ord), (65, 20), wx.NO_BORDER|wx.ALIGN_RIGHT))
            else:
                self.noteBoxes.append(wx.CheckBox(self.panel, ids+i, self.noteNames[i],(self.abs+55, self.ord), (65, 20), wx.NO_BORDER))
            self.ord += 20    
            self.noteBoxes[-1].Bind(wx.EVT_CHECKBOX, self.labelSwap)
        #---------------------------------SettingsBoxes-------------------------------------------    
        self.settingBoxes = []
        self.chordLabels = ["Major", "Minor", "Augm", "Dim", "Maj 7th", "Min 7th", "--", "--", "--", "--"]
        self.intervalLabels= ["Min 2nd","Maj 2nd","Min 3rd","Maj 3rd","Perf 4th","Aug 4th","Perf 5th","Min 6th","Maj 6th","Min 7th"]
        self.abs = 10
        self.ord = 360
        ids = 1500
        for i in range(10):
            if i in [0,2,4,6,8,10]:
                self.settingBoxes.append(wx.CheckBox(self.panel, ids+i, self.intervalLabels[i], (self.abs, self.ord), (200, 20), wx.NO_BORDER))
            else:
                self.settingBoxes.append(wx.CheckBox(self.panel, ids+i, self.intervalLabels[i], (self.abs+80, self.ord), (200, 20), wx.NO_BORDER))
                self.ord += 35    
            self.settingBoxes[-1].Bind(wx.EVT_CHECKBOX, self.printID)
     
    #==================================METHODS==========================================
    def printID(self, evt):
        print evt.GetId()-1000
        self.noteBoxes[0].SetValue(evt.GetInt())
    
    def setTest(self, evt): 
        print evt.GetId()
        self.chosenPige = evt.GetId()
        self.printTextBox(self.textboxes[0],evt.GetString(), 15, wx.NullColour)
        
        if evt.GetId() == 100: #"EADGBE Sequence"
            self.setFonction(pigeEADGBE, testEADGBE, analyseEADGBE, self.descEADGBE)            
        elif evt.GetId() == 101: #"Interval Test"
            self.setFonction(pigeInterval, testInterval, analyseInterval, self.descInterval)
        elif evt.GetId() == 102: #"Chord Test"
            self.setFonction(pigeChord, testChord, analyseChord, self.descChord)                  
        elif evt.GetId() == 103: #"Random Note"
            self.setFonction(pigeNote, testNote, analyseNote, self.descPige)
            
    def loopTest(self):
        if  self.chosenPige == 100: #"EADGBE Sequence"
            self.setFonction(pigeEADGBE, testEADGBE, analyseEADGBE, self.descEADGBE)            
        elif self.chosenPige == 101: #"Interval Test"
            self.setFonction(pigeInterval, testInterval, analyseInterval, self.descInterval)
        elif self.chosenPige == 102: #"Chord Test"
            self.setFonction(pigeChord, testChord, analyseChord, self.descChord)  
        elif self.chosenPige == 103: #"Random Note"
            self.setFonction(pigeNote, testNote, analyseNote, self.descPige)
            
    def setFonction(self, pigeFonction, testFonction, analyseFonction, descriptionFonction):
        self.fonctionPige = pigeFonction()
        text = self.fonctionPige[1]
        print text
        self.printTextBox(self.textboxes[0], text, 30, wx.NullColour)
        self.printTextBox(self.textboxes[2], descriptionFonction, 15, wx.NullColour)
        self.audio.setTest(testFonction)
        self.audio.setAnalyse(analyseFonction) 

    def printTextBox(self, textbox, data, fontSize, color): 
        textbox.Clear()
        textbox.WriteText(data)
        font = wx.Font(fontSize, wx.DEFAULT, wx.NORMAL, wx.BOLD, False)
        textbox.SetStyle(0, len(data), wx.TextAttr(color, wx.NullColour, font))
    
    def checkUncheckAll(self, evt):
        if evt.GetId() == 600:
            if evt.GetInt() == 1:
                for i in range(12):
                    self.noteBoxes[i].SetValue(1)
            elif evt.GetInt() == 0:
                for i in range(12):
                    self.noteBoxes[i].SetValue(0)
                    
        elif evt.GetId() == 601:
            if evt.GetInt() == 1:
                for i in range(10):
                    self.settingBoxes[i].SetValue(1)
            elif evt.GetInt() == 0:
                for i in range(10):
                    self.settingBoxes[i].SetValue(0)

    def labelSwap(self, evt):
        if evt.GetInt() == 1:
            for i in range(10):
                self.settingBoxes[i].SetLabel(self.intervalLabels[i])
        else:
            for i in range(10):
                self.settingBoxes[i].SetLabel(self.chordLabels[i])
            
app = wx.App(False)
mainFrame = MyFrame(None, title='FretMemo', pos=(100,100), size=(560,650))
mainFrame.Show()
app.MainLoop()

#===========================DUMP==============================================
"""        
self.onOffText = wx.StaticText(self.panel, id=-1, label="Audio", 
                                pos=(10,10), size=wx.DefaultSize)
self.onOff = wx.ToggleButton(self.panel, id=-1, label="on / off", 
                            pos=(10,28), size=wx.DefaultSize)
self.incZ = wx.ToggleButton(self.panel, id=-1, label="Attack/Analyse", 
                            pos=(10,150), size=wx.DefaultSize)

# Un event du toggle appelle la methode self.handleAudio
self.onOff.Bind(wx.EVT_TOGGLEBUTTON, self.handleAudio)
self.incZ.Bind(wx.EVT_TOGGLEBUTTON, self.plusOne)

scripts = ["EADGBE Sequence", "Chord Test", "Interval Test", "Random Note"]
self.popup = wx.Choice(self.panel, id=-1, pos=(10,78), size=wx.DefaultSize, choices=scripts)
self.popup.Bind(wx.EVT_CHOICE, self.setTest)
"""    
"""        
def plusOne(self, evt):
    global attack, check
    if evt.GetInt() == 1 or evt.GetInt() == 0:
        setTrue()
    else:
        pass
        
def handleAudio(self, evt):
    # evt.GetInt() retourne 1 si le toggle est a on, 0 s'il est a off
    if evt.GetInt() == 1:
        self.audio.s.start()
    else:
        self.audio.s.stop()

"""    