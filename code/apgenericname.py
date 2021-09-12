from antipatternbase import AntiPatternBase
from statechart import Statechart
import Levenshtein

class APGenericName(AntiPatternBase):
    def __init__(self):
        AntiPatternBase.__init__(self, __class__.__name__)
        self.transitionsFound = []

    def control(self, statechart: Statechart):
        bReturn = False

        for state in statechart.statechart.states:
            
            distance = Levenshtein.distance("state_", state)
            if distance <= 3:
                self.hitCountState += 1
                bReturn = True

        if bReturn:
            self.hitCountStatechart += 1
            statechart.hasGenericName = True
        
        return bReturn
