from pyo import *
from malib import*
import time

pa_list_devices()
print pa_get_default_output()
print pa_get_default_input()
class Audio:
    def __init__(self, parent):
        self.parent = parent
        self.s = Server(sr=44100, nchnls=2, buffersize=512, duplex=1)
        self.s.setInOutDevice(8)
        self.s.boot()
        self.s.start()
        # test and analyse callbacks initilized to None (easy to filter)
        self.testCallback = None
        self.analyseCallback = None
        self.a = Input(chnl=0, mul=0.5)
        self.fa = ButLP(self.a, freq=700).out()
        self.cp = Compress(self.fa*20, thresh=-10, ratio=6)
        self.ying = Yin(self.cp, tolerance=0.2, minfreq=50, maxfreq=750, winsize=2048, mul=0.5)
        self.ad = AttackDetector(self.a, deltime=0.005, cutoff=1, maxthresh=1, minthresh=-45, reltime=0.006)

        self.pat = Pattern(self.doTest, 0.02).play()
        self.add = SDelay(self.ad, 0.25)
        self.tf = TrigFunc(self.add, self.doAnalyse)
 
    def onQuit(self):
        "Shutdown the audio server before quiting the application."
        self.pat.stop()
        self.s.stop()
        time.sleep(0.5)
        self.s.shutdown()
        time.sleep(0.5)

    def doTest(self):
        "Function called by the Pattern object."
        if self.testCallback != None:
            self.result = self.testCallback()
            if self.result == "BRAVO!":
                #self.parent.printTextBox(self.parent.textboxes[1], self.result, 30, "GREEN")
                self.snd = "Ressources/snds/goodAnswer.aif"
                self.sf = SfPlayer(self.snd, speed=[2,2], loop=False, mul=.2).out()
                self.parent.loopTest()
                
            elif self.result == "CHECK!":
                #self.parent.printTextBox(self.parent.textboxes[1], self.result, 30, "YELLOW")
                self.snd = "Ressources/snds/goodAnswer.aif"
                self.sf = SfPlayer(self.snd, speed=[1,1], loop=False, mul=.4).out()
                
            elif self.result == "RECOMMENCEZ!":
                #self.parent.printTextBox(self.parent.textboxes[1], self.result, 30, "RED")
                self.snd = "Ressources/snds/wrongAnswer.aif"
                self.sf = SfPlayer(self.snd, speed=[1,1], loop=False, mul=.1).out()
            self.parent.changeImage(self.result)

    def doAnalyse(self):
        "Function called by the TrigFunc object."
        if self.analyseCallback != None:
            self.analyseCallback(self.ying)

    def setTest(self, func):
        "Sets the test callback."
        self.testCallback = func
        
    def setAnalyse(self, func):
        "Sets the analyse callback."
        self.analyseCallback = func

