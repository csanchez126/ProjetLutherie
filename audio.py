
from pyo import *

def dump():
    pass

class Audio:
    def __init__(self):
        self.s = Server(sr=44100, nchnls=2, buffersize=1024, duplex=1).boot()
        self.s.start()
        # test and analyse callbacks initilized to None (easy to filter)
        self.testCallback = None
        self.analyseCallback = None
        self.a = Input(chnl=0, mul=0.5).out()
        self.ying = Yin(self.a, tolerance=0.2, minfreq=50, maxfreq=800, mul=0.5)
        self.ad = AttackDetector(self.a, deltime=0.005, cutoff=1, maxthresh=1, minthresh=-45, reltime=0.006)

        self.pat = Pattern(self.doTest, 0.02).play()
        self.add = SDelay(self.ad, 0.010)
        self.tf = TrigFunc(self.ad, self.doAnalyse)
        
    # tu peux passer les arguments necessaires aux fonction self.testCallback
    # et self.analyseCallback. J'ai ajoute l'objet Yin en argument de la fonction
    # self.analyseCallback. Vois comment il est recupere dans le fichier fonctionEADGBE.py.
    def doTest(self):
        "Function called by the Pattern object."
        if self.testCallback != None:
            self.testCallback()

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

