from antipatternbase import AntiPatternBase
from statechart import Statechart

class APMissingEvent(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)
        self.transitionsFound = []

    def control(self, statechart: Statechart):
        bReturn = False

        for transition in statechart.statechart.transitions:
            if not transition.event and transition.guard:
                self.transitionsFound.append(transition)
                bReturn = True
                self.hitCountTransition += 1
        
        if bReturn == True:
            self.hitCountStatechart += 1
            statechart.hasMissingEvent = True
        
        return bReturn
