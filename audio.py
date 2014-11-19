
from pyo import *

def dump():
    pass

class Audio:
    def __init__(self):
        self.s = Server(sr=44100, nchnls=2, buffersize=1024, duplex=1).boot()
        self.s.start()    
        self.a = Input(chnl=0, mul=0.5).out()
        self.ying = Yin(self.a, tolerance=0.2, minfreq=50, maxfreq=800, mul=0.5)
        self.ad = AttackDetector(self.a, deltime=0.005, cutoff=1, maxthresh=1, minthresh=-45, reltime=0.006)


        self.pat = Pattern(dump, 0.02).play()
        self.add = SDelay(self.ad, 0.010)
        self.tf = TrigFunc(self.ad, dump)
        
    def setTest(self, func):
        self.pat.function = func
        
    def setAnalyse(self, func):
        self.tf.function = func

