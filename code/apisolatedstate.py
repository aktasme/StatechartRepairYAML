from antipatternbase import AntiPatternBase
from statechart import Statechart

class APIsolatedState(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)
        self.transitionsFound = []

    def control(self, statechart: Statechart):
        bReturn = False

        for state in statechart.statechart.states:                     
            if False:
                self.hitCountState += 1
                bReturn = True

        if bReturn:
            self.hitCountStatechart += 1
            statechart.hasIsolatedState = True
        
        return bReturn
