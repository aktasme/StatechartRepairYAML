from srcommonlog import SRCommonLog
from srstatechart import SRStatechart

class AntiPatternBase(SRCommonLog):
    def __init__(self):
        self.name = ""

    def control(statechart: SRStatechart):
        return False

    def repair(statechart: SRStatechart):
        return False

    def toPrintableString(self):
        return 'AntiPattern: {}'.format(self.name)