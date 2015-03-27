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
        self.cbPanel = wx.Panel(self.panel, size=(150,700))
        self.textboxPanel = wx.Panel(self.panel)
        self.line = wx.StaticLine(self.panel, -1, size=(1,-1), style=wx.LI_VERTICAL) #Checkbox and TextBox separation
        self.setHint = None
        #GUI Boxes
        self.mainBox = wx.BoxSizer(wx.HORIZONTAL)
        self.textboxBox = wx.BoxSizer(wx.VERTICAL) #Main Textbox Box, Right side of GUI
        self.topTextboxBox = wx.BoxSizer(wx.HORIZONTAL) #Top Half Box of Right Side
        self.leftTopTextboxBox = wx.BoxSizer(wx.VERTICAL)#Left Half of Top  Box of Right Side (Top Left Quarter)
        self.topLeftTopTextboxBox = wx.BoxSizer(wx.VERTICAL) #TopHalf Of TopLeftQuarter
        self.botLeftTopTextboxBox = wx.BoxSizer(wx.VERTICAL) #BottomHalf Of TopLeftQuarter
        self.rightTopTextboxBox = wx.BoxSizer(wx.VERTICAL) #Right half of Top Box of Right Side (Top Right Quarter)
        self.bottomTextboxBox = wx.BoxSizer(wx.VERTICAL) #Bottom Half of Right side of GUI
        
        #Check/Uncheck All Toggles
        self.chUncheckNotes = wx.ToggleButton(self.cbPanel, id=600, label="Check/Uncheck All", pos=(10,320), size=wx.DefaultSize) #For Notes
        self.chUncheckNotes.Bind(wx.EVT_TOGGLEBUTTON, self.checkUncheckAll)
        self.chUncheckSettings = wx.ToggleButton(self.cbPanel, id=601, label="Check/Uncheck All", pos=(10,630), size=wx.DefaultSize) #For Shapes
        self.chUncheckSettings.Bind(wx.EVT_TOGGLEBUTTON, self.checkUncheckAll)
        #Run Button
        self.runButton = wx.Button(self.cbPanel, id=602, label="Run Test", pos=(10,10), size=wx.DefaultSize) 
        self.runButton.Bind(wx.EVT_BUTTON, self.runTest)
        
        #Debug Toggle
        self.testCheck = wx.ToggleButton(self.cbPanel, id=-1, label="Check", pos=(10,660), size=wx.DefaultSize)
        self.testCheck.Bind(wx.EVT_TOGGLEBUTTON, self.check)
    
        #=======================RESULT IMAGES============================
        self.checkBMP = wx.Image('icons/check.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.wrongBMP = wx.Image('icons/wrong.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.bravoBMP = wx.Image('icons/bravo.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.blankBMP = wx.Image('icons/blank.bmp', wx.BITMAP_TYPE_BMP).ConvertToBitmap()
        self.displayImage = wx.StaticBitmap(self.textboxPanel, -1, self.blankBMP)
        #=========================MenuBar===============================
        self.menuBar = wx.MenuBar() #Main MenuBar
        self.menu1 = wx.Menu() #First DropDown
        self.menuTestNames = ["&EADGBE Sequence", "&Interval Test", "&Chord Test", "&Random Note"]
        for i in range (4): #Append Test names to Firs DropDown
            self.menu1.Append(i+100, self.menuTestNames[i],"")
            self.Bind(wx.EVT_MENU, self.setTestDesc, id=i+100)
        self.menuBar.Append(self.menu1, "&Tests")
        
        self.menu2 = wx.Menu()#Second Drop Down
        self.menu2.Append(200, "Standard Relative", "", wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.setRelative, id=200)
        self.menu2.Append(201, "Tuning Relative", "", wx.ITEM_RADIO)
        self.Bind(wx.EVT_MENU, self.setRelative, id=201)
        self.menu2.AppendSeparator()
        self.menuTunings = ["-4st", "-3st", "-2st", "-1st", "Standard", "+1st", "+2st", "+3st", "+4st"]
        for i in range (9): #Append Test names to Firs DropDown
            self.menu2.Append(i+300, self.menuTunings[i],"", wx.ITEM_RADIO)
            self.Bind(wx.EVT_MENU, self.setTuning, id=i+300)
        self.menuBar.Append(self.menu2, "&Tunings")
        
        self.SetMenuBar(self.menuBar)
        #========================Variables===============================
        self.audio = Audio(self)
        self.chosenPige = None
        self.fonctionPige = None

        #TestDescriptions
        self.descPige = "User must play the randomly selected note on any octave."
        self.descInterval = "User must play the selected interval in an ascending order, starting from the randomly selected note"
        self.descChord = "User must play the four notes of the selected chord in an ascending order. The shape refers to the structure of the open chord shapes."
        self.descEADGBE = "User must play the standard tuning sequence from the randomly selected fret, starting from the lowest string."
        
        #==================================LABELS============================================
        self.testNote = wx.StaticText(self.textboxPanel, id=-1, label="Play:", pos=(190,10), size=wx.DefaultSize)
        self.testShape = wx.StaticText(self.textboxPanel, id=-1, label="Shape:", pos=(190,10), size=wx.DefaultSize)
        self.testResult = wx.StaticText(self.textboxPanel, id=-1, label="Result:", pos=(370,10), size=wx.DefaultSize)
        self.testDesc = wx.StaticText(self.textboxPanel, id=-1, label="Description:", pos=(190,230), size=wx.DefaultSize)
        self.testNotes = wx.StaticText(self.cbPanel, id=-1, label="Notes:", pos=(10,45), size=wx.DefaultSize)
        self.testSettings = wx.StaticText(self.cbPanel, id=-1, label="Settings:", pos=(10,360), size=wx.DefaultSize)
        
        self.topLeftTopTextboxBox.Add(self.testNote, 0, wx.LEFT, 5) #Append Note Label to TopHalf of TopLeftQuarter
        self.botLeftTopTextboxBox.Add(self.testShape, 0, wx.LEFT, 5) #Append Shape Label to BotHalf of TopLeftQuarter
        self.rightTopTextboxBox.Add(self.testResult, 0, wx.LEFT, 5) #Append Result Label to TopRightQuarter
        self.bottomTextboxBox.Add(self.testDesc, 0, wx.LEFT, 5) #Append Description Label to BottomHalf
        #================================TEXTBOXES============================================        
        self.textboxes = []
        ids = 2000
        self.textboxes.append(wx.TextCtrl(self.textboxPanel, ids,size=(350,100), style = wx.TE_MULTILINE | wx.TE_RICH2)) #Note TextBox
        self.topLeftTopTextboxBox.Add(self.textboxes[-1], 1, wx.ALL|wx.EXPAND, 5)
        
        self.textboxes.append(wx.TextCtrl(self.textboxPanel, ids+1,size=(350,100), style = wx.TE_MULTILINE | wx.TE_RICH2)) #NoteParam TextBox
        self.botLeftTopTextboxBox.Add(self.textboxes[-1], 1, wx.ALL|wx.EXPAND, 5)
        
        #self.textboxes.append(wx.TextCtrl(self.textboxPanel, ids+2, size=(250,250),style = wx.TE_RICH2)) #Result TextBox
        #self.rightTopTextboxBox.Add(self.textboxes[-1], 0, wx.ALL|wx.EXPAND, 5)
        self.rightTopTextboxBox.Add(self.displayImage, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_VERTICAL, 15)


        self.textboxes.append(wx.TextCtrl(self.textboxPanel, ids+2, style = wx.TE_MULTILINE | wx.TE_RICH2)) #Description TextBox
        self.bottomTextboxBox.Add(self.textboxes[-1], 1, wx.ALL|wx.EXPAND, 5)
        
        #================================CHECKBOXES============================================ 
        #-----------------------------------------------------------NoteBoxes---------------------------------------------------------------------------------    
        self.noteBoxes = []
        self.noteNames = ["C","C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab", "A", "A#/Bb", "B"]
        self.abs = 10
        self.ord = 70
        ids = 1000
        for i in range(12):
            if i in [0,2,4,5,7,9,11]:
                self.noteBoxes.append(wx.CheckBox(self.cbPanel, ids+i, self.noteNames[i],(self.abs, self.ord), (30, 20), wx.NO_BORDER|wx.ALIGN_RIGHT))
            else:
                self.noteBoxes.append(wx.CheckBox(self.cbPanel, ids+i, self.noteNames[i],(self.abs+55, self.ord), (53, 20), wx.NO_BORDER))
            self.ord += 20    
            self.noteBoxes[-1].Bind(wx.EVT_CHECKBOX, self.cbUpdate)
        #---------------------------------------------------------SettingsBoxes--------------------------------------------------------------------------------    
        self.settingBoxes = []
        self.chordLabels = ["Maj", "Min", "Aug", "Dim7", "Maj7", "Dom7", "mMaj7", "mMin7", "Maj6", "Min6", "Sus2", "Sus4"]
        self.intervalLabels= ["Min 2nd","Maj 2nd","Min 3rd","Maj 3rd","Perf 4th","Aug 4th","Perf 5th","Min 6th","Maj 6th","Min 7th","Maj 7th", "--"]
        self.abs = 10
        self.ord = 390
        ids = 1500
        for i in range(12):
            if i in [0,2,4,6,8,10]:
                self.settingBoxes.append(wx.CheckBox(self.cbPanel, ids+i, self.intervalLabels[i], (self.abs, self.ord), (60, 20), wx.NO_BORDER))
            else:
                self.settingBoxes.append(wx.CheckBox(self.cbPanel, ids+i, self.intervalLabels[i], (self.abs+80, self.ord), (60, 20), wx.NO_BORDER))
                self.ord += 35    
            self.settingBoxes[-1].Bind(wx.EVT_CHECKBOX, self.cbUpdate)
            
        self.chordHintBox = wx.CheckBox(self.cbPanel, 1600, "Chord Hint", (10, 600), (100, 20), wx.NO_BORDER)
        self.chordHintBox.Bind(wx.EVT_CHECKBOX, self.hintToggle)
        
        #==============================GUI BOX HIERARCHY==================================
        self.leftTopTextboxBox.Add(self.topLeftTopTextboxBox, 1, wx.EXPAND) 
        self.leftTopTextboxBox.Add(self.botLeftTopTextboxBox, 1, wx.EXPAND)
        self.topTextboxBox.Add(self.leftTopTextboxBox, 1, wx.ALL|wx.EXPAND, 5)
        self.topTextboxBox.Add(self.rightTopTextboxBox, 0, wx.ALL|wx.EXPAND, 5)
        self.textboxBox.Add(self.topTextboxBox, 1, wx.ALL|wx.EXPAND, 5)
        self.textboxBox.Add(self.bottomTextboxBox, 1, wx.ALL|wx.EXPAND, 10)
        self.textboxPanel.SetSizer(self.textboxBox)
        
        self.mainBox.Add(self.cbPanel, 0, wx.ALL, 5)
        self.mainBox.Add(self.line, 0, wx.LEFT|wx.TOP|wx.BOTTOM|wx.EXPAND, 10)
        self.mainBox.Add(self.textboxPanel, 1, wx.ALL|wx.EXPAND, 5)
        self.panel.SetSizer(self.mainBox)

        # Bind le "X" de la fenetre a la methode OnClose
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        self.SetMinSize((700, 650))
        self.SetSize((701,761))
        
        

    #==================================METHODS==========================================
    def setRelative(self, evt):
        global relative
        if self.menu2.IsChecked(200):
            relative = 1
            print "StandardRelative"
        elif self.menu2.IsChecked(201):
            relative = 2
            print "Tuning Relative"
      
    def setTuning(self, evt):
        global tuning
        if evt.GetId() == 300:
            tuning = -4
        elif evt.GetId() == 301:
            tuning = -3
        elif evt.GetId() == 302:
            tuning = -2
        elif evt.GetId() == 303:
            tuning = -1
        elif evt.GetId() == 304:
            pass  
        elif evt.GetId() == 305:
            tuning = 1
        elif evt.GetId() == 306:
            tuning = 2
        elif evt.GetId() == 307:
            tuning = 3
        elif evt.GetId() == 308:
            tuning = 4
        print tuning

    def OnClose(self, evt):
        "Shutdown the audio server and destroy the window."
        self.audio.onQuit()
        self.Destroy()

    def setTestDesc(self, evt): 
        self.chosenPige = evt.GetId()
        self.printTextBox(self.textboxes[0],evt.GetString(), 15, wx.NullColour)
        
        if evt.GetId() == 100: #"EADGBE Sequence"
            self.printTextBox(self.textboxes[2], self.descEADGBE , 15, wx.NullColour)      
        elif evt.GetId() == 101: #"Interval Test"
            self.printTextBox(self.textboxes[2], self.descInterval, 15, wx.NullColour)
            self.labelSwap(evt)
        elif evt.GetId() == 102: #"Chord Test"
            self.printTextBox(self.textboxes[2], self.descChord, 15, wx.NullColour) 
            self.labelSwap(evt)                  
        elif evt.GetId() == 103: #"Random Note"
            self.printTextBox(self.textboxes[2], self.descPige, 15, wx.NullColour) 
            
    def loopTest(self):
        if  self.chosenPige == 100: #"EADGBE Sequence"
            self.setFonction(pigeEADGBE, testEADGBE, analyseEADGBE)            
        elif self.chosenPige == 101: #"Interval Test"
            self.setFonction(pigeInterval, testInterval, analyseInterval)
        elif self.chosenPige == 102: #"Chord Test"
            self.setFonction(pigeChord, testChord, analyseChord)  
        elif self.chosenPige == 103: #"Random Note"
            self.setFonction(pigeNote, testNote, analyseNote)
            
    def setFonction(self, pigeFonction, testFonction, analyseFonction):
        self.fonctionPige = pigeFonction()
        text1 = self.fonctionPige[1]
        text2 = self.fonctionPige[2]
        print text1, text2
        self.printTextBox(self.textboxes[0], text1, 35, wx.NullColour)
        self.printTextBox(self.textboxes[1], text2, 30, wx.NullColour)
        self.audio.setTest(testFonction)
        self.audio.setAnalyse(analyseFonction) 

    def printTextBox(self, textbox, data, fontSize, color): 
        textbox.Clear()
        textbox.WriteText(data)
        font = wx.Font(fontSize, wx.DEFAULT, wx.NORMAL, wx.BOLD, False)
        textbox.SetStyle(0, len(data), wx.TextAttr(color, wx.NullColour, font))
        
    def runTest(self, evt):
        if self.chosenPige == 100: #"EADGBE Sequence"
            self.setFonction(pigeEADGBE, testEADGBE, analyseEADGBE)            
        elif self.chosenPige == 101: #"Interval Test"
            self.setFonction(pigeInterval, testInterval, analyseInterval)
            self.labelSwap(evt)
        elif self.chosenPige == 102: #"Chord Test"
            self.setFonction(pigeChord, testChord, analyseChord)
            self.labelSwap(evt)
            if self.setHint == 1:
                self.printTextBox(self.textboxes[2], chordHint[self.fonctionPige[3]], 30, wx.NullColour) 
            elif self.setHint == 0:
                self.printTextBox(self.textboxes[2], self.descChord, 15, wx.NullColour)         
        elif self.chosenPige == 103: #"Random Note"
            self.setFonction(pigeNote, testNote, analyseNote)
    
    def cbUpdate(self, evt):
        del notePool[:]
        del settingsPool[:]
        for i in self.noteBoxes:
            if i.IsChecked() == 1:
                notePool.append(i.GetId()-1000)
        for i in self.settingBoxes:
            if i.IsChecked() == 1:
                settingsPool.append(i.GetId()-1500)
        
        if len(notePool) == 0:
            self.runButton.Disable()
        elif len(settingsPool) == 0:
            self.runButton.Disable()
        else:
            self.runButton.Enable()

    def checkUncheckAll(self, evt):
        if evt.GetId() == 600: #600s = ChUncheck button IDS
            if evt.GetInt() == 1:
                for i in range(12):
                    self.noteBoxes[i].SetValue(1)
            elif evt.GetInt() == 0:
                for i in range(12):
                    self.noteBoxes[i].SetValue(0)
                    
        elif evt.GetId() == 601:
            if evt.GetInt() == 1:
                for i in range(12):
                    self.settingBoxes[i].SetValue(1)
            elif evt.GetInt() == 0:
                for i in range(12):
                    self.settingBoxes[i].SetValue(0)    
        self.cbUpdate(evt)

    def labelSwap(self, evt):
        if evt.GetId() == 101:#"Interval Test"
            for i in range(12):
                self.settingBoxes[i].SetLabel(self.intervalLabels[i])
        elif evt.GetId() == 102: #"Chord Test"
            for i in range(12):
                self.settingBoxes[i].SetLabel(self.chordLabels[i])
   
    def hintToggle(self,evt):
        if evt.GetInt() == 1:
            if self.chosenPige == 102: #Chord Test
                self.setHint = 1
                print self.setHint
        elif evt.GetInt() == 0:
            if self.chosenPige == 102: #Chord Test
                self.setHint = 0
                print self.setHint
                
    #Debug Method
    def check(self, evt):
        if evt.GetInt() == 1 or evt.GetInt() == 0:
            setTrue()
        else:
            pass

            
app = wx.App(False)
mainFrame = MyFrame(None, title='FretMemo', pos=(100,100), size=(700,700))
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

def printID(self, evt):
    print evt.GetId()-1000
    self.noteBoxes[0].SetValue(evt.GetInt())
"""    